import os
import shutil
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
    QLabel, QSpinBox, QMessageBox
)


from natsort import natsorted
class DatasetDivider(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Dataset Divider")
        self.resize(300, 200)

        self.image_folder = ""
        self.label_folder = ""

        layout = QVBoxLayout()

        self.select_images_btn = QPushButton("1. Select Images Folder")
        self.select_images_btn.clicked.connect(self.select_images_folder)
        layout.addWidget(self.select_images_btn)

        self.select_labels_btn = QPushButton("2. Select Labels Folder")
        self.select_labels_btn.clicked.connect(self.select_labels_folder)
        layout.addWidget(self.select_labels_btn)

        layout.addWidget(QLabel("Select % for training data:"))

        self.percent_spinbox = QSpinBox()
        self.percent_spinbox.setRange(1, 99)
        self.percent_spinbox.setValue(90)
        layout.addWidget(self.percent_spinbox)

        self.divide_btn = QPushButton("Divide")
        self.divide_btn.clicked.connect(self.divide_dataset)
        layout.addWidget(self.divide_btn)

        self.setLayout(layout)

    def select_images_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Images Folder")
        if folder:
            self.image_folder = folder

    def select_labels_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Labels Folder")
        if folder:
            self.label_folder = folder

    def divide_dataset(self):
        if not self.image_folder or not self.label_folder:
            QMessageBox.warning(self, "Warning", "Please select both folders.")
            return

        # ✅ Natural sort
        images = natsorted([
            f for f in os.listdir(self.image_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])

        split_percent = self.percent_spinbox.value()
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

        QMessageBox.information(self, "Success", "Dataset successfully divided!")


if __name__ == "__main__":
    app = QApplication([])
    window = DatasetDivider()
    window.show()
    app.exec()

