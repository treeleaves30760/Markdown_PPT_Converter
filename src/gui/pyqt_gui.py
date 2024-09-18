import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QProgressBar, QMessageBox
)

import src.converter.converter as converter


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 640, 640)
        self.setWindowTitle("Markdown to PPT Converter By Hsu Po Hsiang")
        self.create_widgets()

    def create_widgets(self):
        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a text area
        self.textarea = QTextEdit(self)
        self.textarea.setPlaceholderText("Enter Markdown here...")
        layout.addWidget(self.textarea)

        # Import markdown file button
        import_button = QPushButton("Import Markdown File", self)
        import_button.clicked.connect(self.import_file)
        layout.addWidget(import_button)

        # Convert button
        convert_button = QPushButton("Convert", self)
        convert_button.clicked.connect(self.convert)
        layout.addWidget(convert_button)

        # Progress bar
        self.progress = QProgressBar(self)
        layout.addWidget(self.progress)

        # Open output folder button
        open_folder_button = QPushButton("Open Output Folder", self)
        open_folder_button.clicked.connect(self.open_output_folder)
        layout.addWidget(open_folder_button)

    def import_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open file", "", "Markdown files (*.md);;Text files (*.txt)"
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.textarea.setPlainText(file.read())

    def convert(self):
        md_content = self.textarea.toPlainText()
        output_filename, ok = QFileDialog.getSaveFileName(
            self, "Save file", "", "PowerPoint files (*.pptx)"
        )
        if ok:
            Converter = converter.MarkdownToPptConverter(
                md_content, output_filename)
            self.progress.setValue(50)  # Simulating a step in the conversion
            Converter.convert()
            self.progress.setValue(100)
            QMessageBox.information(
                self, "Conversion Completed", f"File has been converted and saved as {output_filename}"
            )

    def open_output_folder(self):
        output_folder_path = os.path.abspath(os.getcwd())
        try:
            os.startfile(output_folder_path)  # For Windows
        except AttributeError:
            # For MacOS and Linux, handle differently
            if sys.platform == "darwin":
                os.system(f"open {output_folder_path}")
            else:
                os.system(f"xdg-open {output_folder_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())
