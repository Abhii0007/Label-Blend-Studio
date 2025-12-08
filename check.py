import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout,
    QLineEdit, QScrollArea, QFrame, QInputDialog, QMessageBox
)
from PyQt6.QtCore import Qt

SNIPPET_FILE = "snippets.json"

class SnippetManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Snippet Inserter")
        self.resize(900, 600)

        self.snippets = self.load_snippets()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # ===== Left Panel =====
        left_panel = QVBoxLayout()

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search snippets...")
        self.search_bar.textChanged.connect(self.filter_buttons)
        left_panel.addWidget(self.search_bar)

        # Scroll area for snippet buttons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.snippet_container = QVBoxLayout()
        self.snippet_container.setAlignment(Qt.AlignTop)

        container_widget = QFrame()
        container_widget.setLayout(self.snippet_container)
        scroll_area.setWidget(container_widget)
        left_panel.addWidget(scroll_area)

        # Save Snippet button
        self.save_button = QPushButton("➕ Save Snippet")
        self.save_button.clicked.connect(self.save_snippet)
        left_panel.addWidget(self.save_button)

        # Snippet buttons
        self.buttons = {}
        for name, code in self.snippets.items():
            self.add_snippet_button(name, code)

        # ===== Right Panel (Text area) =====
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Write or edit your code here...")

        main_layout.addLayout(left_panel, 2)
        main_layout.addWidget(self.text_area, 5)

    def add_snippet_button(self, title, code):
        """Create and add a new snippet button"""
        if title in self.buttons:
            QMessageBox.warning(self, "Duplicate", f"A snippet named '{title}' already exists.")
            return

        btn = QPushButton(title)
        btn.clicked.connect(lambda checked, c=code: self.insert_code(c))
        self.snippet_container.addWidget(btn)
        self.buttons[title] = btn
        self.snippets[title] = code
        self.save_snippets_to_file()

    def insert_code(self, code):
        cursor = self.text_area.textCursor()
        cursor.insertText(code + "\n")

    def filter_buttons(self, text):
        text = text.lower()
        for title, button in self.buttons.items():
            button.setVisible(text in title.lower())

    def save_snippet(self):
        code = self.text_area.toPlainText().strip()
        if not code:
            QMessageBox.warning(self, "Empty", "Write code in the text area before saving.")
            return

        name, ok = QInputDialog.getText(self, "Snippet Name", "Enter name for your snippet:")
        if ok and name:
            self.add_snippet_button(name.strip(), code)

    def save_snippets_to_file(self):
        with open(SNIPPET_FILE, "w") as f:
            json.dump(self.snippets, f, indent=2)

    def load_snippets(self):
        if os.path.exists(SNIPPET_FILE):
            with open(SNIPPET_FILE, "r") as f:
                return json.load(f)
        return {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SnippetManager()
    window.show()
    sys.exit(app.exec())
