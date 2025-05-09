import sys
import os
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout,
    QWidget, QSpinBox, QHBoxLayout, QLineEdit, QMessageBox
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PIL import Image, ImageQt
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from PIL import ImageDraw
from PySide6.QtWidgets import QPushButton
import cv2


def merge_polygons(polygons):
    if len(polygons) < 2:
        return polygons
    all_points = np.vstack(polygons)
    hull = cv2.convexHull(all_points)
    return [hull.tolist()]

def extract_and_merge_polygons(mask: Image.Image, class_id: int, image_size=(1000, 1000)):
    np_mask = np.array(mask)
    gray = np_mask[:, :, 3]  # Alpha channel
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    polygons = []
    for contour in contours:
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) >= 3:
            polygons.append(approx)

    merged = merge_polygons(polygons)
    
    label_lines = []
    for polygon in merged:
        norm_polygon = []
        for point in polygon:
            x, y = point[0]
            nx = round(x / image_size[0], 6)
            ny = round(y / image_size[1], 6)
            norm_polygon.extend([nx, ny])
        label_lines.append(f"{class_id} " + " ".join(map(str, norm_polygon)))

    return label_lines







class ImageGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Image Generator")
        self.setFixedSize(800, 700)

        self.cutout_images = []
        self.background_images = []

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(800, 600)

        select_cutouts_btn = QPushButton("Select Cutout Images")
        select_cutouts_btn.clicked.connect(self.select_cutouts)

        select_background_btn = QPushButton("Select Background Images")
        select_background_btn.clicked.connect(self.select_background)

        # Range inputs for cutout sizes
        self.min_size_input = QSpinBox()
        self.min_size_input.setRange(1, 1000)
        self.min_size_input.setValue(50)
        self.max_size_input = QSpinBox()
        self.max_size_input.setRange(1, 1000)
        self.max_size_input.setValue(150)

        # Number of images input
        self.num_images_input = QSpinBox()
        self.num_images_input.setRange(1, 1000)
        self.num_images_input.setValue(5)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Min Cutout Size:"))
        size_layout.addWidget(self.min_size_input)
        size_layout.addWidget(QLabel("Max Cutout Size:"))
        size_layout.addWidget(self.max_size_input)

        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("Number of Images to Save:"))
        count_layout.addWidget(self.num_images_input)

        generate_btn = QPushButton("Generate & Save Images")
        generate_btn.clicked.connect(self.generate_and_save_images)

        generate_single_btn = QPushButton("Generate Random Image (No Save)")
        generate_single_btn.clicked.connect(self.generate_image_no_save)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(size_layout)
        layout.addLayout(count_layout)
        layout.addWidget(select_cutouts_btn)
        layout.addWidget(select_background_btn)
        layout.addWidget(generate_btn)
        layout.addWidget(generate_single_btn)
        #-------------------1:31------------------\
        self.segmentation_button = QPushButton("Generate Segmentation Images")
        self.segmentation_button.clicked.connect(self.generate_and_save_segmentations)
        layout.addWidget(self.segmentation_button)  # Adjust as per your layout

        #-------------------4:10------------------\
        self.starting_image_input = QSpinBox()
        self.starting_image_input.setMinimum(1)
        self.starting_image_input.setValue(1)
        self.starting_image_input.setPrefix("Start #: ")
        
        layout.addWidget(QLabel("Starting Image No.:"))
        layout.addWidget(self.starting_image_input)

        
        #-------------------4:10------------------/







        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.bounding_boxes = []


    



    def generate_and_save_segmentations(self):
        try:
            count = int(self.num_images_input.text())
            start_index = int(self.starting_image_input.value())
        except ValueError:
            return

        if not self.cutout_images or not self.background_images:
            return

        os.makedirs("output/images", exist_ok=True)
        os.makedirs("output/labels_seg", exist_ok=True)

        def generate(i):
            image_index = start_index + i
            bg = random.choice(self.background_images).copy().resize((1000, 1000))
            result = bg.copy()
            label_lines = []

            for cutout, class_id in self.cutout_images:
                cutout_copy = cutout.copy()
                size = random.randint(self.min_size_input.value(), self.max_size_input.value())
                resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)
                angle = random.randint(0, 359)
                rotated = resized.rotate(angle, expand=True)

                w, h = rotated.size
                x = random.randint(0, 1000 - w)
                y = random.randint(0, 1000 - h)

                result.paste(rotated, (x, y), rotated)

                full_mask = Image.new("RGBA", (1000, 1000), (0, 0, 0, 0))
                full_mask.paste(rotated, (x, y), rotated)

                label_lines.extend(
                    extract_and_merge_polygons(full_mask, class_id, image_size=(1000, 1000))
                )

            # Save image and label using the new index
            result.save(f"output/images/image{image_index}.png")
            with open(f"output/labels_seg/image{image_index}.txt", "w") as f:
                f.write("\n".join(label_lines))

        with ThreadPoolExecutor() as executor:
            executor.map(generate, range(count))

        self.notify_images_saved(count)


#------------------changes made------------------\
    def select_cutouts(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Cutout Images", "", "Images (*.png *.jpg *.jpeg)")
        for file in files:
            image = Image.open(file).convert("RGBA")
            # Use filename (without extension) as class label index
            class_id = len(self.cutout_images)  # or use mapping if desired
            self.cutout_images.append((image, class_id))
        self.generate_image_no_save()

#------------------changes made------------------/          
    def select_background(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Background Images", "", "Images (*.jpg *.png *.jpeg)")
        if files:
            self.background_images = [Image.open(f).convert("RGBA").resize((800, 600)) for f in files]
            self.show_image(self.background_images[0])  # Show the first selected background

        
    def generate_random_image(self, size=(800, 600)):
        if not self.cutout_images or not self.background_images:
            return None

        background = random.choice(self.background_images).copy()
        result = background.resize(size)

        min_size = self.min_size_input.value()
        max_size = self.max_size_input.value()
        if min_size > max_size:
            min_size, max_size = max_size, min_size

        for cutout, class_id in self.cutout_images:  # Unpack the tuple (image, class_id)
            cutout = cutout.copy()  # Now `cutout` is the PIL.Image
            w = random.randint(min_size, max_size)
            cutout = cutout.resize((w, w), Image.Resampling.LANCZOS)

            # Apply random rotation
            angle = random.randint(0, 359)
            cutout_rotated = cutout.rotate(angle, expand=True)

            # Get size after rotation
            w, h = cutout_rotated.size
            x = random.randint(0, size[0] - w)
            y = random.randint(0, size[1] - h)

            result.paste(cutout_rotated, (x, y), cutout_rotated)

            # Now, you can store the bounding box and class ID in a list for YOLO labeling
            # Calculate normalized values for YOLO (x_center, y_center, width, height)
            bbox = (x + w / 2) / size[0], (y + h / 2) / size[1], w / size[0], h / size[1]
            self.bounding_boxes.append((class_id, *bbox))  # Add to the list

        return result



    def generate_image_no_save(self):
        image = self.generate_random_image(size=(800, 600))
        if image:
            self.show_image(image)
        else:
            QMessageBox.warning(self, "Warning", "Select cutout and background images first.")

    


    def generate_and_save_images(self):
        try:
            count = int(self.num_images_input.text())
        except ValueError:
            return

        min_size = self.min_size_input.value()
        max_size = self.max_size_input.value()

        if min_size > max_size or not self.cutout_images or not self.background_images:
            return

        # Create required folders
        image_dir = os.path.join("output", "images")
        label_dir = os.path.join("output", "labels")
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)

        def generate_and_save(i):
            background = random.choice(self.background_images).copy().resize((1000, 1000))
            result = background.copy()

            bboxes = []  # Store bounding box for this image

            for cutout_image, class_id in self.cutout_images:
                cutout_copy = cutout_image.copy()
                size = random.randint(min_size, max_size)
                cutout_resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)

                angle = random.randint(0, 359)
                cutout_rotated = cutout_resized.rotate(angle, expand=True)

                w, h = cutout_rotated.size
                x = random.randint(0, 1000 - w)
                y = random.randint(0, 1000 - h)

                result.paste(cutout_rotated, (x, y), cutout_rotated)

                # Bounding box in YOLO format
                cx = (x + w / 2) / 1000
                cy = (y + h / 2) / 1000
                nw = w / 1000
                nh = h / 1000
                bboxes.append(f"{class_id} {cx:.6f} {cy:.6f} {nw:.6f} {nh:.6f}")

            image_name = f"Image{i+1}.png"
            label_name = f"Image{i+1}.txt"

            result.save(os.path.join(image_dir, image_name))

            with open(os.path.join(label_dir, label_name), "w") as f:
                f.write("\n".join(bboxes))

        with ThreadPoolExecutor() as executor:
            executor.map(generate_and_save, range(count))

        self.notify_images_saved(count)



    def notify_images_saved(self, count):
        # Notify user after saving all images
        QMessageBox.information(self, "Done", f"{count} images have been saved successfully!")
        
    
    def show_image(self, image):
        qimage = ImageQt.ImageQt(image.convert("RGBA"))
        pixmap = QPixmap.fromImage(QImage(qimage))
        self.label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageGenerator()
    window.show()
    sys.exit(app.exec())
