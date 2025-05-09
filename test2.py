from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,
    QWidget, QHBoxLayout
)
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt
import sys
import cv2
import numpy as np
import random

def random_light_color_2():
    base_2 = [random.randint(150, 255) for _ in range(3)]
    base_2[random.randint(0, 2)] = 255
    return tuple(base_2)

def load_segmentations_2(txt_file_2, img_width_2, img_height_2):
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

def overlay_masks_2(image_2, masks_2):
    darkened_2 = (image_2 * 0.7).astype(np.uint8)
    overlay_2 = darkened_2.copy()
    colors_2 = {}

    for class_id_2, polygon_2 in masks_2:
        if class_id_2 not in colors_2:
            colors_2[class_id_2] = random_light_color_2()
        color_2 = colors_2[class_id_2]

        cv2.fillPoly(overlay_2, [polygon_2], color_2)
        cv2.polylines(darkened_2, [polygon_2], isClosed=True, color=color_2, thickness=2)

        x_2, y_2 = polygon_2[0]
        cv2.putText(darkened_2, str(class_id_2), (x_2, y_2 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_2, 2)

    final_2 = cv2.addWeighted(overlay_2, 0.4, darkened_2, 0.6, 0)
    return final_2

def cv2_to_pixmap_2(img_2):
    h_2, w_2, ch_2 = img_2.shape
    bytes_per_line_2 = ch_2 * w_2
    qimg_2 = QImage(img_2.data, w_2, h_2, bytes_per_line_2, QImage.Format_BGR888)
    return QPixmap.fromImage(qimg_2)

class ZoomableGraphicsView_2(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def wheelEvent(self, event_2):
        zoom_in_2 = 1.25
        zoom_out_2 = 0.8
        factor_2 = zoom_in_2 if event_2.angleDelta().y() > 0 else zoom_out_2
        self.scale(factor_2, factor_2)

class ControlWidget_2(QWidget):
    def __init__(self, load_img_callback_2, load_seg_callback_2):
        super().__init__()
        layout_2 = QHBoxLayout()
        self.btn_img_2 = QPushButton("Select Image")
        self.btn_seg_2 = QPushButton("Select Segment TXT")
        self.btn_img_2.clicked.connect(load_img_callback_2)
        self.btn_seg_2.clicked.connect(load_seg_callback_2)
        layout_2.addWidget(self.btn_img_2)
        layout_2.addWidget(self.btn_seg_2)
        self.setLayout(layout_2)

class SegmentViewer_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segmentation Viewer with Zoom")

        self.image_2 = None
        self.image_path_2 = None

        self.container_2 = QWidget(self)
        self.setCentralWidget(self.container_2)

        self.scene_2 = QGraphicsScene()
        self.view_2 = ZoomableGraphicsView_2()
        self.view_2.setScene(self.scene_2)

        self.control_widget_2 = ControlWidget_2(self.load_image_2, self.load_segments_2)

        self.container_layout_2 = QHBoxLayout(self.container_2)
        self.container_layout_2.addWidget(self.control_widget_2)
        self.container_layout_2.addWidget(self.view_2)

        
    def load_image_2(self):
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path_2:
            self.image_path_2 = path_2
            self.image_2 = cv2.imread(path_2)
            self.show_image_2(self.image_2)

    def load_segments_2(self):
        if self.image_2 is None:
            return
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select YOLO Segment TXT", "", "Text Files (*.txt)")
        if path_2:
            h_2, w_2 = self.image_2.shape[:2]
            masks_2 = load_segmentations_2(path_2, w_2, h_2)
            masked_2 = overlay_masks_2(self.image_2.copy(), masks_2)
            self.show_image_2(masked_2)

    def show_image_2(self, img_2):
        self.scene_2.clear()
        pixmap_2 = cv2_to_pixmap_2(img_2)
        self.pixmap_item_2 = QGraphicsPixmapItem(pixmap_2)
        self.scene_2.addItem(self.pixmap_item_2)
        self.view_2.fitInView(self.pixmap_item_2, Qt.KeepAspectRatio)

# Run app
if __name__ == "__main__":
    app_2 = QApplication(sys.argv)
    viewer_2 = SegmentViewer_2()
    viewer_2.resize(800, 600)
    viewer_2.show()
    sys.exit(app_2.exec())
