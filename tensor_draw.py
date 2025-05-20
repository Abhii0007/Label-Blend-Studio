from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QListWidget, QListWidgetItem, QGraphicsView,
    QGraphicsScene, QDialog, QTextEdit, QFormLayout, QLineEdit
)
from PySide6.QtCore import Qt
import sys

class LayerWidget(QWidget):
    def __init__(self, layer_type="Dense", default_units=1, default_activation="linear"):
        super().__init__()
        self.layer_type = layer_type
        self.units_input = QLineEdit(str(default_units))
        self.activation_input = QLineEdit(default_activation)

        layout = QFormLayout()
        layout.addRow("Units:", self.units_input)
        layout.addRow("Activation:", self.activation_input)
        self.setLayout(layout)
        self.setFixedSize(200, 80)
        self.setStyleSheet("background-color: #e0f7fa; border: 1px solid #00796b; border-radius: 8px;")

    def get_layer_code(self):
        units = self.units_input.text()
        activation = self.activation_input.text()
        return f"Dense({units}, activation='{activation}')"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neural Network GUI Designer")
        self.setMinimumSize(600, 400)

        self.canvas_layout = QVBoxLayout()
        self.layer_widgets = []

        # Left: Toolbox
        self.toolbox = QListWidget()
        self.toolbox.addItem("Regression Layer")
        self.toolbox.setFixedWidth(150)

        # Center: Canvas
        self.canvas = QWidget()
        self.canvas.setLayout(self.canvas_layout)
        self.canvas.setStyleSheet("background-color: #fafafa; border: 1px solid #ccc;")
        
        # Right: Export Button
        self.export_button = QPushButton("Export TensorFlow Code")
        self.export_button.clicked.connect(self.show_code)

        layout = QHBoxLayout()
        layout.addWidget(self.toolbox)
        layout.addWidget(self.canvas)
        layout.addWidget(self.export_button)

        self.setLayout(layout)

        self.toolbox.itemDoubleClicked.connect(self.add_layer)

    def add_layer(self, item: QListWidgetItem):
        text = item.text()
        if text == "Regression Layer":
            widget = LayerWidget()
            self.canvas_layout.addWidget(widget)
            self.layer_widgets.append(widget)

    def show_code(self):
        code_lines = [
            "from tensorflow.keras.models import Sequential",
            "from tensorflow.keras.layers import Dense",
            "",
            "model = Sequential(["
        ]

        for w in self.layer_widgets:
            code_lines.append(f"    {w.get_layer_code()},")
        code_lines.append("])")

        dialog = QDialog(self)
        dialog.setWindowTitle("Exported Code")
        layout = QVBoxLayout()
        text = QTextEdit("\n".join(code_lines))
        layout.addWidget(text)
        dialog.setLayout(layout)
        dialog.resize(500, 300)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
