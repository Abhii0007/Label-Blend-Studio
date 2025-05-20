import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl


class MyWebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def featurePermissionRequested(self, securityOrigin, feature):
        print(f"Permission requested: {feature}")
        self.setFeaturePermission(
            securityOrigin, feature, QWebEnginePage.PermissionGrantedByUser
        )


class PhotopeaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Photopea Embedder")

        self.webview = QWebEngineView()
        self.webview.setPage(MyWebPage(self))
        self.webview.load(QUrl("https://www.photopea.com"))

        open_external_btn = QPushButton("Open in Browser (Full Features)")
        open_external_btn.clicked.connect(self.open_in_browser)

        layout = QVBoxLayout()
        layout.addWidget(self.webview)
        layout.addWidget(open_external_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.resize(1200, 800)

    def open_in_browser(self):
        QDesktopServices.openUrl(QUrl("https://www.photopea.com"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhotopeaApp()
    window.show()
    sys.exit(app.exec())
