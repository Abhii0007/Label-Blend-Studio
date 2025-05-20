import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--log-level=3"
import sys,io

import shutil
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout,
    QWidget, QSpinBox, QHBoxLayout, QLineEdit, QMessageBox
)
from PySide6.QtGui import QPixmap, QImage,QPainter
from PySide6.QtCore import Qt,QUrl
from PIL import Image, ImageQt
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from PIL import ImageDraw
from PySide6.QtWidgets import QPushButton
import cv2
from PySide6.QtGui import QDesktopServices

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,
    QWidget, QHBoxLayout
)
from natsort import natsorted

from PySide6.QtWebEngineWidgets import QWebEngineView 
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings



# ---------- Zoomable View ----------
class ZoomableGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def wheelEvent(self, event):
        zoom_in = 1.25
        zoom_out = 0.8
        factor = zoom_in if event.angleDelta().y() > 0 else zoom_out
        self.scale(factor, factor)


from window_test2 import Ui_MainWindow
class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_MainWindow()
        self.form.setupUi(self)
        
       
        self.cutout_images = []
        self.background_images = []
        self.showMaximized()
        self.form.actionExit.triggered.connect(self.close)
        
        
        
        self.form.pushButton_select_cutouts_btn.clicked.connect(self.select_cutouts)
        self.form.pushButton_select_background_btn.clicked.connect(self.select_background)
        self.form.pushButton_generate_btn.clicked.connect(self.generate_and_save_images)
        self.form.pushButton_generate_single_btn.clicked.connect(self.generate_image_no_save)
        self.form.pushButton_segmentation_button.clicked.connect(self.generate_and_save_segmentations)
        
        self.form.pushButton_open_folder.clicked.connect(self.open_folder)
        self.form.toolButton_open_box_folder.clicked.connect(self.select_box_folder)
        self.form.toolButton_toolButton_open_segment_folder.clicked.connect(self.select_segment_folder)
        self.form.actionNew_Project.triggered.connect(self.new_window)
        self.bounding_boxes = []
        
        #-------------------Box Viewer------------------\
        self.cv_img = None
        self.label_path = None
        self.image = None
        self.form.pushButton_btn_select_image.clicked.connect(self.load_image)
        self.form.pushButton_btn_select_label.clicked.connect(self.load_labels)
        self.form.pushButton_default.clicked.connect(self.reset_res)
        self.view = ZoomableGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        
        self.container_layout = QHBoxLayout(self.form.widget_box)
       
        self.container_layout.addWidget(self.view)
        #-------------------End------------------/

        #-------------------Segment Viewer------------------\
        self.image = None
        self.image_path = None
        self.form.pushButton_btn_image2.clicked.connect(self.load_image_2)
        self.form.pushButton_btn_txt2.clicked.connect(self.load_segments_2)
        self.form.pushButton_default_res.clicked.connect(lambda: self.form.spinBox_resolution_epsilon.setValue(10))
        
        self.form.lineEdit_box_location.setText(os.getcwd())
        self.form.lineEdit_segment_location.setText(os.getcwd())
        # Set the size of the view
        self.scene_2 = QGraphicsScene()
        self.view_2 = ZoomableGraphicsView()
        self.view_2.setScene(self.scene_2)
        #self.view_2.setGeometry(0, 0, 800, 600)  # Set the size of the view
        
        self.container_layout_2 = QHBoxLayout(self.form.widget_segment)
       
        self.container_layout_2.addWidget(self.view_2)
        #-------------------End------------------/
        #--------------------Mannual Data Splitter--------------------\
        self.image_folder = ""
        self.label_folder = ""
        self.form.comboBox_split.setCurrentIndex(2) #default train/val
        self.form.toolButton_Select_image_folder.clicked.connect(self.select_images_folder)
        self.form.toolButton_Select_label_folder.clicked.connect(self.select_labels_folder)
        self.form.pushButton_force_split.clicked.connect(self.divide_dataset)
        self.form.pushButton_splitter_default.clicked.connect(lambda: self.form.comboBox_split.setCurrentIndex(2))
        #-------------------End--------------------------------------/

        
        
        
        
        self.form.horizontalSlider_quality.valueChanged.connect(self.update_quality_label)
        self.form.spinBox_num_quality.valueChanged.connect(self.update_quality_slider)
        self.form.comboBox_profile.currentIndexChanged.connect(self.update_image_settings)
        
        
        self.form.pushButton_show_in_browser.clicked.connect(self.open_photopea_url)
        
        profile = QWebEngineProfile.defaultProfile()
        settings = self.form.webEngineView.settings()
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)  # Allow remote URLs in local content
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)    # Allow local file URLs
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        profile.downloadRequested.connect(self.handle_download)
        
        
        
        #---------------------------New Features------------------------\
        self.form.listWidget.currentRowChanged.connect(self.on_list_item_selected)
        self.form.toolButton_next.setText("\u2190")
        self.form.toolButton_next.clicked.connect(self.show_next_image)
        self.form.toolButton_prev.clicked.connect(self.show_prev_image)
            
        #------------------------------end------------------------------/
        
    def on_list_item_selected(self, index):
        if 0 <= index < len(self.background_images):
            self.current_index = index
            
            self.show_image(self.background_images[self.current_index][1])  # PIL Image
            
            print("Background path:", self.background_images[self.current_index][0])
            self.form.lineEdit_background_src.setText(self.background_images[self.current_index][0])
        
        
            self.generate_image_no_save()

    def show_next_image(self):
        if self.background_images and self.current_index < len(self.background_images) - 1:
            self.current_index += 1
            self.form.listWidget.setCurrentRow(self.current_index)  # Update selection

    def show_prev_image(self):
        if self.background_images and self.current_index > 0:
            self.current_index -= 1
            self.form.listWidget.setCurrentRow(self.current_index)  # Update selection
    # Update selection













    def handle_download(self, download):
        filename = download.downloadFileName()
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", filename)
        if path:
            try:
                download.setDownloadDirectory(os.path.dirname(path))
                download.setDownloadFileName(os.path.basename(path))
            except AttributeError:
                pass  # fallback for older versions
            download.accept()
            
            
    def open_photopea_url(self):
        url = "https://www.photopea.com#%7B%22files%22%3A%5B%22https%3A%2F%2Fwww.photopea.com%2Fapi%2Fimg2%2Fpug.png%22%5D%2C%22environment%22%3A%7B%7D%7D"
        QDesktopServices.openUrl(QUrl(url))
        
        
        
    def update_image_settings(self, index):
        if index == 1:
            self.form.spinBox_width.setValue(3840)
            self.form.spinBox_height.setValue(2160)
        elif index == 2:
            self.form.spinBox_width.setValue(1920)
            self.form.spinBox_height.setValue(1920)
        elif index == 3:
            self.form.spinBox_width.setValue(1280)
            self.form.spinBox_height.setValue(1280)
        elif index == 4:
            self.form.spinBox_width.setValue(640)
            self.form.spinBox_height.setValue(640)
        elif index == 5:
            self.form.spinBox_width.setValue(512)
            self.form.spinBox_height.setValue(512)
        elif index == 6:
            self.form.spinBox_width.setValue(256)
            self.form.spinBox_height.setValue(256)
        elif index == 7:
            self.form.spinBox_width.setValue(224)
            self.form.spinBox_height.setValue(224)
        else:
            self.form.spinBox_width.setValue(1024)
            self.form.spinBox_height.setValue(1024)

    def update_quality_slider(self, value):
        self.form.horizontalSlider_quality.setValue(value)
        
    def update_quality_label(self, value):
       
        self.form.spinBox_num_quality.setValue(value)
        
    def select_box_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        #print(folder_path)
        self.form.lineEdit_box_location.setText(folder_path)
        
    def select_segment_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        #print(folder_path)
        self.form.lineEdit_segment_location.setText(folder_path)
        
    def reset_res(self):
        
        self.form.horizontalSlider_quality.setValue(90)
        self.form.comboBox_profile.setCurrentIndex(0)
        
        
        
    def new_window(self):
        global window1
        
        window1 = window()
        window1.show()

    def open_folder(self):
        # Relative folder path (adjust if needed)
        folder_path = os.path.abspath("./")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
    
   
    def open_box_folder(self):
        #os.makedirs("output_box/images", exist_ok=True)
        #os.makedirs("output_box/labels", exist_ok=True)
        
        folder_path = os.path.abspath(self.form.lineEdit_box_location.text()+"/Output_box")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
        
    def open_segment_folder(self):
        #toolButton_toolButton_open_segment_folder
        folder_path = os.path.abspath(self.form.lineEdit_segment_location.text()+"/Output_segment")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
        
    def merge_polygons(self,polygons):
        if len(polygons) < 2:
            return polygons
        all_points = np.vstack(polygons)
        hull = cv2.convexHull(all_points)
        return [hull.tolist()]

    def extract_and_merge_polygons(self,mask: Image.Image, class_id: int, image_size=(1000, 1000)):
        np_mask = np.array(mask)
        gray = np_mask[:, :, 3]  # Alpha channel
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        polygons = []
        for contour in contours:
            #epsilon defalt value is 0.01
            value = widget.form.spinBox_resolution_epsilon.value()*0.001
            epsilon = value * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) >= 3:
                polygons.append(approx)
        merged = self.merge_polygons(polygons)
        
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


    def generate_and_save_segmentations(self):
        width = self.form.spinBox_width.value()
        height = self.form.spinBox_height.value()

        try:
            count = int(self.form.spinBox_num_images_input.text())
            start_index = int(self.form.spinBox_starting_image_input.value())
        except ValueError:
            return

        if not self.cutout_images or not self.background_images:
            return

        folder = self.form.lineEdit_segment_location.text()
        if not folder:
            return

        image_dir = os.path.join(folder, "Output_segment", "images")
        label_dir = os.path.join(folder, "Output_segment", "labels")
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)

        def generate(index):
            image_index = start_index + index
            background_path, bg_pil = random.choice(self.background_images)
            background = bg_pil.copy().resize((width, height))

            result = background.copy()
            label_lines = []

            for cutout_image, class_id in self.cutout_images:
                cutout_copy = cutout_image.copy()

                size = random.randint(
                    self.form.spinBox_min_size_input.value(),
                    self.form.spinBox_max_size_input.value()
                )
                resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)
                angle = random.randint(0, 359)
                rotated = resized.rotate(angle, expand=True)

                w, h = rotated.size
                x = random.randint(0, width - w)
                y = random.randint(0, height - h)

                # Paste onto result
                result.paste(rotated, (x, y), rotated)

                # Prepare mask for polygon extraction
                mask = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                mask.paste(rotated, (x, y), rotated)

                polygons = self.extract_and_merge_polygons(mask, class_id, image_size=(width, height))
                label_lines.extend(polygons)

            # Save image
            output_image = result.convert("RGB")
            image_name = f"Image{image_index}.jpg"
            label_name = f"Image{image_index}.txt"

            output_image.save(os.path.join(image_dir, image_name), format="JPEG", quality=self.form.horizontalSlider_quality.value())
            with open(os.path.join(label_dir, label_name), "w") as f:
                f.write("\n".join(label_lines))

        # Generate images in parallel
        with ThreadPoolExecutor() as executor:
            executor.map(generate, range(count))

        # Optional dataset division
        if self.form.checkBox.isChecked():
            self.image_folder = image_dir
            self.label_folder = label_dir
            self.divide_dataset(checks=True)

        self.notify_images_saved_seg(count)


    #------------------changes made------------------\
    def select_cutouts(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Cutout Images", "", "Images (*.png *.jpg *.jpeg)")
        for file in files:
            image = Image.open(file).convert("RGBA")
            class_id = len(self.cutout_images)
            self.cutout_images.append((image, class_id))  # store as (PIL.Image, class_id)
        self.generate_image_no_save()  # show random preview


    def select_background(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Background Images", "", "Images (*.jpg *.png *.jpeg)"
        )
        if files:
            self.background_images = []
            self.form.listWidget.clear()

            for file_path in files:
                pil_img = Image.open(file_path).convert("RGBA").resize((1605, 830))
                # Store tuple (file_path, pil_img)
                self.background_images.append((file_path, pil_img))

                # Make thumbnail for QListWidget
                thumb = pil_img.copy().resize((100, 60))
                buffer = io.BytesIO()
                thumb.save(buffer, format="PNG")
                qimg = QImage.fromData(buffer.getvalue(), "PNG")
                pixmap = QPixmap.fromImage(qimg)

                from PySide6.QtWidgets import QListWidgetItem
                item = QListWidgetItem(file_path.split("/")[-1])
                item.setIcon(pixmap)
                self.form.listWidget.addItem(item)

            self.current_index = 0
            self.show_image(self.background_images[self.current_index][1])  # Pass the PIL image



    def generate_random_image(self, size=(1605, 830)):
        if not self.cutout_images or not self.background_images:
            return None

        # Use currently selected background (not random)
        background_path = self.background_images[self.current_index][0]
        background = self.background_images[self.current_index][1].copy().resize(size)


        
        print("Background index:", self.current_index)
        print("Background path:", self.background_images[self.current_index][0])
        self.form.lineEdit_background_src.setText(background_path)


        min_size = self.form.spinBox_min_size_input.value()
        max_size = self.form.spinBox_max_size_input.value()
        if min_size > max_size:
            min_size, max_size = max_size, min_size

        self.bounding_boxes = []

        for cutout, class_id in self.cutout_images:
            cutout = cutout.copy()
            w = random.randint(min_size, max_size)
            cutout = cutout.resize((w, w), Image.Resampling.LANCZOS)

            angle = random.randint(0, 359)
            cutout_rotated = cutout.rotate(angle, expand=True)

            w, h = cutout_rotated.size
            x = random.randint(0, size[0] - w)
            y = random.randint(0, size[1] - h)

            background.paste(cutout_rotated, (x, y), cutout_rotated)

            bbox = (x + w / 2) / size[0], (y + h / 2) / size[1], w / size[0], h / size[1]
            self.bounding_boxes.append((class_id, *bbox))

        return background






    def generate_image_no_save(self):
        image = self.generate_random_image()
        if image is not None:
            qim = ImageQt.ImageQt(image)  # PIL.Image -> QImage
            pixmap = QPixmap.fromImage(qim)
            self.form.label.setPixmap(pixmap.scaled(self.form.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    
    

  

    def generate_and_save_images(self):
        try:
            count = int(self.form.spinBox_num_images_input.text())
            start_index = int(self.form.spinBox_starting_image_input.value())
        except ValueError:
            return

        min_size = self.form.spinBox_min_size_input.value()
        max_size = self.form.spinBox_max_size_input.value()

        if min_size > max_size or not self.cutout_images or not self.background_images:
            return

        folder_path = self.form.lineEdit_box_location.text()
        if not folder_path:
            return

        # Create output directories
        image_dir = os.path.join(folder_path, "Output_box", "images")
        label_dir = os.path.join(folder_path, "Output_box", "labels")
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)

        width = self.form.spinBox_width.value()
        height = self.form.spinBox_height.value()
        quality = self.form.horizontalSlider_quality.value()

        def generate_and_save(i):
            image_index = start_index + i

            # ✅ Correct way to get a PIL background image
            bg_path, bg_pil = random.choice(self.background_images)
            background = bg_pil.copy().resize((width, height))
            result = background.copy()
            bboxes = []

            for cutout_image, class_id in self.cutout_images:
                cutout_copy = cutout_image.copy()
                size = random.randint(min_size, max_size)
                cutout_resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)

                angle = random.randint(0, 359)
                cutout_rotated = cutout_resized.rotate(angle, expand=True)

                w, h = cutout_rotated.size
                if w >= width or h >= height:
                    continue  # Skip if cutout is too large

                x = random.randint(0, width - w)
                y = random.randint(0, height - h)

                result.paste(cutout_rotated, (x, y), cutout_rotated)

                cx = (x + w / 2) / width
                cy = (y + h / 2) / height
                nw = w / width
                nh = h / height
                bboxes.append(f"{class_id} {cx:.6f} {cy:.6f} {nw:.6f} {nh:.6f}")

            image_name = f"Image{image_index}.jpg"
            label_name = f"Image{image_index}.txt"

            # Save image
            result.convert("RGB").save(os.path.join(image_dir, image_name), format="JPEG", quality=quality)

            # Save label
            with open(os.path.join(label_dir, label_name), "w") as f:
                f.write("\n".join(bboxes))

        with ThreadPoolExecutor() as executor:
            executor.map(generate_and_save, range(count))

        if self.form.checkBox.isChecked():
            self.image_folder = image_dir
            self.label_folder = label_dir
            self.divide_dataset(checks=True)

        self.notify_images_saved_box(count)


    def notify_images_saved_box(self, count):
        # Notify user after saving all images
        import time
                
        msg = QMessageBox(self)
        msg.setText(f"{count} images have been saved successfully!")
        msg.addButton("Open Folder", QMessageBox.AcceptRole)
        open_btn = msg.addButton("Done", QMessageBox.ActionRole)
        msg.exec(), None if msg.clickedButton() == open_btn else self.open_box_folder()


    
    def notify_images_saved_seg(self, count):
        # Notify user after saving all images
        import time
                
        msg = QMessageBox(self)
        msg.setText(f"{count} images have been saved successfully!")
        msg.addButton("Open Folder", QMessageBox.AcceptRole)
        open_btn = msg.addButton("Done", QMessageBox.ActionRole)
        msg.exec(), None if msg.clickedButton() == open_btn else self.open_segment_folder()
    
        
    
    
    '''def show_image(self, image):
        qimage = ImageQt.ImageQt(image.convert("RGBA"))
        pixmap = QPixmap.fromImage(QImage(qimage))
        self.form.label.setPixmap(pixmap)'''
    def show_image(self, pil_img):
        # Expecting a PIL Image already loaded and resized
        buffer = io.BytesIO()
        pil_img.save(buffer, format="PNG")
        qimg = QImage.fromData(buffer.getvalue(), "PNG")
        pixmap = QPixmap.fromImage(qimg)
        self.form.label.setPixmap(pixmap)  # Display in QLabel
    # Display in QLabel (adjust as needed)


    #------------------Box Viewer------------------\
    def load_bboxes(self,txt_file, img_width, img_height):
        bboxes = []
        with open(txt_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])
                x_min = int((x_center - width / 2) * img_width)
                y_min = int((y_center - height / 2) * img_height)
                x_max = int((x_center + width / 2) * img_width)
                y_max = int((y_center + height / 2) * img_height)
                bboxes.append((class_id, x_min, y_min, x_max, y_max))
        return bboxes
            
    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.image_path = path
            self.cv_img = cv2.imread(path)
            self.display_image(self.cv_img)

    def random_light_color(self):
        base = [random.randint(120, 200) for _ in range(3)]
        base[random.randint(0, 2)] = 255
        return tuple(base)

    def load_labels(self):
        if self.cv_img is None:
            return

        txt_path, _ = QFileDialog.getOpenFileName(self, "Select YOLO TXT", "", "Text Files (*.txt)")
        if txt_path:
            h, w = self.cv_img.shape[:2]
            bboxes = self.load_bboxes(txt_path, w, h)

            img_copy = self.cv_img.copy()
            overlay = img_copy.copy()
            cv2.addWeighted(overlay, 0.2, img_copy, 0.5, 0, img_copy)

            colors = {}
            for class_id, x_min, y_min, x_max, y_max in bboxes:
                if class_id not in colors:
                    colors[class_id] = self.random_light_color()
                color = colors[class_id]
                cv2.rectangle(img_copy, (x_min, y_min), (x_max, y_max), color, 2)
                cv2.putText(img_copy, str(class_id), (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            self.display_image(img_copy)

    def display_image(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        self.scene.clear()
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.view.setSceneRect(pixmap.rect())
        
        
        
  

    #------------------Segment Viewer------------------\
    

    def load_image_2(self):
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path_2:
            self.image_path_2 = path_2
            self.image_2 = cv2.imread(path_2)
            self.show_image_2(self.image_2)
            
    def random_light_color_2(self):
        base_2 = [random.randint(150, 255) for _ in range(3)]
        base_2[random.randint(0, 2)] = 255
        return tuple(base_2)

    def overlay_masks_2(self,image_2, masks_2):
        darkened_2 = (image_2 * 0.7).astype(np.uint8)
        overlay_2 = darkened_2.copy()
        colors_2 = {}

        for class_id_2, polygon_2 in masks_2:
            if class_id_2 not in colors_2:
                colors_2[class_id_2] = self.random_light_color_2()
            color_2 = colors_2[class_id_2]

            cv2.fillPoly(overlay_2, [polygon_2], color_2)
            cv2.polylines(darkened_2, [polygon_2], isClosed=True, color=color_2, thickness=2)

            x_2, y_2 = polygon_2[0]
            cv2.putText(darkened_2, str(class_id_2), (x_2, y_2 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_2, 2)

        final_2 = cv2.addWeighted(overlay_2, 0.4, darkened_2, 0.6, 0)
        return final_2
    
    def load_segmentations_2(self,txt_file_2, img_width_2, img_height_2):
        masks_2 = []
        with open(txt_file_2, 'r') as f_2:
            for line_2 in f_2:
                parts_2 = line_2.strip().split()
                class_id_2 = int(parts_2[0])
                coords_2 = list(map(float, parts_2[1:]))
                points_2 = np.array([
                    [int(coords_2[i] * img_width_2), int(coords_2[i + 1] * img_height_2)]
                    for i in range(0, len(coords_2), 2)
                ], np.int32)
                masks_2.append((class_id_2, points_2))
        return masks_2
    
    def load_segments_2(self):
        if self.image_2 is None:
            return
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select YOLO Segment TXT", "", "Text Files (*.txt)")
        if path_2:
            h_2, w_2 = self.image_2.shape[:2]
            masks_2 = self.load_segmentations_2(path_2, w_2, h_2)
            masked_2 = self.overlay_masks_2(self.image_2.copy(), masks_2)
            self.show_image_2(masked_2)
            
    def cv2_to_pixmap_2(self,img_2):
        h_2, w_2, ch_2 = img_2.shape
        bytes_per_line_2 = ch_2 * w_2
        qimg_2 = QImage(img_2.data, w_2, h_2, bytes_per_line_2, QImage.Format_BGR888)
        return QPixmap.fromImage(qimg_2)


    def show_image_2(self, img_2):
        self.scene_2.clear()
        pixmap_2 = self.cv2_to_pixmap_2(img_2)
        self.pixmap_item_2 = QGraphicsPixmapItem(pixmap_2)
        self.scene_2.addItem(self.pixmap_item_2)
        self.view_2.fitInView(self.pixmap_item_2, Qt.KeepAspectRatio)
        
    #--------------------Mannual Data Splitter--------------------\
    def select_images_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Images Folder")
        if folder:
            self.image_folder = folder
            

    def select_labels_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Labels Folder")
        if folder:
            self.label_folder = folder

    def divide_dataset(self,checks = False):
        
        train_combobox_index = self.form.comboBox_split.currentIndex()
        split_percent = 80
        
        
        if train_combobox_index == 0:
            split_percent = 95
        elif train_combobox_index == 1:
            split_percent = 90
        
        elif train_combobox_index == 3:
            split_percent = 70
        elif train_combobox_index == 4:
            split_percent = 50
        elif train_combobox_index == 5:
            split_percent = 30
        
        else:
            split_percent = 80

        
        
        if not self.image_folder or not self.label_folder:
            QMessageBox.warning(self, "Warning", "Please select both folders.")
            return

       
        images = natsorted([
            f for f in os.listdir(self.image_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])

      
        split_index = int(len(images) * (split_percent / 100.0))

        train_images = images[:split_index]
        val_images = images[split_index:]

        for subfolder in ['train', 'val']:
            os.makedirs(os.path.join(self.image_folder, subfolder), exist_ok=True)
            os.makedirs(os.path.join(self.label_folder, subfolder), exist_ok=True)

        def move_files(image_list, subfolder):
            for img_file in image_list:
                base_name = os.path.splitext(img_file)[0]
                label_file = base_name + ".txt"

                src_img = os.path.join(self.image_folder, img_file)
                dst_img = os.path.join(self.image_folder, subfolder, img_file)
                if os.path.exists(src_img):
                    shutil.move(src_img, dst_img)

                src_label = os.path.join(self.label_folder, label_file)
                dst_label = os.path.join(self.label_folder, subfolder, label_file)
                if os.path.exists(src_label):
                    shutil.move(src_label, dst_label)

        move_files(train_images, "train")
        move_files(val_images, "val")

        if checks==False:
            
            QMessageBox.information(self, "Success", "Dataset successfully divided!")

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    sys.exit(app.exec())