import hashlib
import tkinter as tk
from tkinter import messagebox
import threading
from os import system as cmd
from PIL import Image, ImageTk

def zipping():
    try:
        cmd("7zip\\7za.exe a pack.zip pack\\*")
        messagebox.showinfo("Успіх", "Архів zip створено успішно.")
        calculate_sha1()
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося створити архів zip: {e}")

def get_sha1(file_name):
    try:
        with open(file_name, "rb") as f:
            sha1 = hashlib.sha1()
            for chunk in iter(lambda: f.read(4096), b""):
                sha1.update(chunk)
        return sha1.hexdigest()
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося розрахувати SHA1-хеш: {e}")
        return None

def calculate_sha1():
    sha1 = get_sha1("pack.zip")
    if sha1:
        sha1_label.config(text=f"SHA1: {sha1}")
        root.clipboard_clear()
        root.clipboard_append(sha1)
        messagebox.showinfo("Успіх", f"SHA1 скопійовано до буфера обміну.")

def handle_button_click():
    threading.Thread(target=zipping).start()

root = tk.Tk()
root.title("Hudoliy ResourcePacker GUI for Windows")
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)
root.iconbitmap("src/pack.ico")

logo = Image.open("src/logo.png")
logo = logo.resize((500, int(500 * logo.height / logo.width)), Image.BICUBIC)
logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=20)

button = tk.Button(root, text="Запакувати та обчислити SHA1", command=handle_button_click)
button.pack(pady=20)

sha1_label = tk.Label(root, text="SHA1 буде відображено тут")
sha1_label.pack()

root.mainloop()
