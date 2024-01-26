import hashlib
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal
from os import system as cmd
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QMimeData
from PyQt6.QtGui import QClipboard

class Worker(QThread):
    finished = pyqtSignal(str, str)

    def run(self):
        try:
            if sys.platform == "win32":
                cmd("7zip\\7za.exe a pack.zip .\pack\*")
            elif sys.platform == "linux" or sys.platform == "linux2":
                cmd("7z a pack.zip .\pack\*")
            elif sys.platform == "darwin":
                cmd("7z a pack.zip .\pack\*")
            self.finished.emit("Успіх", "Архів zip створено успішно.")
        except Exception as e:
            self.finished.emit("Помилка", f"Не вдалося створити архів zip: {e}")

    def get_sha1(self, file_name):
        try:
            with open(file_name, "rb") as f:
                sha1 = hashlib.sha1()
                for chunk in iter(lambda: f.read(4096), b""):
                    sha1.update(chunk)
            return sha1.hexdigest()
        except Exception as e:
            self.finished.emit("Помилка", f"Не вдалося розрахувати SHA1-хеш: {e}")
            return None

    def calculate_sha1(self):
        sha1 = self.get_sha1("pack.zip")
        if sha1:
            with open("sha1.txt", "w") as f:
                f.write(sha1)
                f.close
            return sha1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hudoliy ResourcePacker GUI for Windows (Qt6)")
        self.setFixedSize(517, 250)
        self.setWindowIcon(QIcon("./src/pack.ico"))

        self.worker = Worker()
        self.worker.finished.connect(self.show_message)

        self.button = QPushButton("Запакувати та обчислити SHA1")
        self.button.clicked.connect(self.handle_button_click)

        self.sha1_label = QLabel("SHA1 буде відображено тут")

        logo = QPixmap("src/logo.png")
        logo = logo.scaledToWidth(500)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(logo)

        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.addWidget(self.button)
        layout.addWidget(self.sha1_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_button_click(self):
        self.worker.start()

    def show_message(self, title, message):
        reply = QMessageBox.information(self, title, message)
        if reply == QMessageBox.StandardButton.Ok and title == "Успіх" and message == "Архів zip створено успішно.":
            sha1 = self.worker.calculate_sha1()
            if sha1:
                self.sha1_label.setText(f"SHA1: {sha1}")
                clipboard = QApplication.clipboard()
                mimeData = QMimeData()
                mimeData.setText(sha1)
                clipboard.setMimeData(mimeData)
                self.show_message("Успіх", f"SHA1 скопійовано до буфера обміну. Та записано до файлу sha1.txt.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
