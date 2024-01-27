import hashlib
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QMenu, QDialog
from PyQt6.QtCore import QThread, pyqtSignal
from os import system as cmd
from PyQt6.QtGui import QIcon, QPixmap, QAction
from PyQt6.QtCore import QMimeData
import webbrowser
import requests
import subprocess

current_version = '2.2'

class Worker(QThread):
    finished = pyqtSignal(str, str)

    def run(self):
        try:
            if sys.platform == "win32":
                cmd("7zip\\7za.exe a pack.zip .\pack\*")
            elif sys.platform == "linux" or sys.platform == "linux2":
                cmd("7zip/7zz-linux a pack.zip ./pack/*")
            elif sys.platform == "darwin":
                cmd("7zip/7zz-macos a pack.zip ./pack/*")
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

        if sys.platform == "win32":
            self.setWindowTitle("Hudoliy ResourcePacker GUI for Windows (Qt6)")
        elif sys.platform == "linux" or sys.platform == "linux2":
            self.setWindowTitle("Hudoliy ResourcePacker GUI for Linux (Qt6)")
        elif sys.platform == "darwin":
            self.setWindowTitle("Hudoliy ResourcePacker GUI for macOS (Qt6)")    
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

        menu_bar = QMenuBar(self)
        help_menu = QMenu("Допомога", self)
        github_action = QAction("GitHub", self)
        github_action.triggered.connect(lambda: webbrowser.open('https://github.com/xxanqw/hudoliy-resourcepack'))
        about_action = QAction("Про програму", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(github_action)
        help_menu.addAction(about_action)
        menu_bar.addMenu(help_menu)
        update_menu = QMenu("Оновлення", self)
        check_update_action = QAction("Перевірити оновлення", self)
        check_update_action.triggered.connect(self.open_update_dialog)
        update_menu.addAction(check_update_action)
        menu_bar.addMenu(update_menu)
        self.setMenuBar(menu_bar)

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
    
    def show_about_dialog(self):
        QMessageBox.about(self, "Про програму", "Hudoliy ResourcePacker GUI (Qt6)\n\nАвтор: xxanqw\n\nGitHub: https://github.com/xxanqw")
        
    def open_update_dialog(self):
        self.update_dialog = UpdateDialog(self)
        self.update_dialog.check_updates()
        self.update_dialog.exec()

class UpdateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.label = QLabel("Перевірка оновлень...")
        self.version = QLabel(f"Ваша версія: {current_version}")
        self.update_button = QPushButton("Оновити")
        self.update_button.clicked.connect(self.on_update)
        self.update_button.setEnabled(False)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.version)
        self.layout.addWidget(self.update_button)
        self.setLayout(self.layout)
        self.setFixedSize(200,100)
        self.setWindowTitle("Перевірка на оновлення")

    def check_updates(self):
        latest_version = self.get_version()
        if latest_version and latest_version != current_version:
            self.label.setText(f"Доступне оновлення: {latest_version}")
            self.update_button.setEnabled(True)
        else:
            self.label.setText("Оновлень немає.")

    def on_update(self):
        self.run_update_script()

    def run_update_script(self):
        try:
            subprocess.Popen(['python', './src/update.py'])
            sys.exit()
        except Exception as e:
            print(f"Error running update script: {e}")
    
    def get_version(self):
        try:
            response = requests.get('https://versionmanager.xserv.pp.ua/hpgui.ver')
            response.raise_for_status()
            return response.text.strip()
        except Exception as e:
            print(f"Error getting version: {e}")
            return None

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())