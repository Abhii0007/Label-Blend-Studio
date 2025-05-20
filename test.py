import sys
import cv2
import numpy as np
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
)
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt


# ---------- Bounding Box Loader ----------
def load_bboxes(txt_file, img_width, img_height):
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


def random_light_color():
    base = [random.randint(120, 200) for _ in range(3)]
    base[random.randint(0, 2)] = 255
    return tuple(base)


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


# ---------- Main App ----------
class BoundingBoxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Viewer with Mouse Control")

        self.view = ZoomableGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.btn_image = QPushButton("Load Image")
        self.btn_labels = QPushButton("Load TXT Labels")

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.btn_image)
        layout.addWidget(self.btn_labels)
        self.setLayout(layout)

        self.btn_image.clicked.connect(self.load_image)
        self.btn_labels.clicked.connect(self.load_labels)

        self.cv_img = None
        self.image_path = ""

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.image_path = path
            self.cv_img = cv2.imread(path)
            self.display_image(self.cv_img)

    def load_labels(self):
        if self.cv_img is None:
            return

        txt_path, _ = QFileDialog.getOpenFileName(self, "Select YOLO TXT", "", "Text Files (*.txt)")
        if txt_path:
            h, w = self.cv_img.shape[:2]
            bboxes = load_bboxes(txt_path, w, h)

            img_copy = self.cv_img.copy()
            overlay = img_copy.copy()
            cv2.addWeighted(overlay, 0.2, img_copy, 0.5, 0, img_copy)

            colors = {}
            for class_id, x_min, y_min, x_max, y_max in bboxes:
                if class_id not in colors:
                    colors[class_id] = random_light_color()
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


# ---------- Run App ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = BoundingBoxApp()
    viewer.resize(900, 700)
    viewer.show()
    sys.exit(app.exec())
