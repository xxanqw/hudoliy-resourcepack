import sys
from os import system as cmd, getcwd as dir, chdir as cd
from os.path import basename as cdn
from os import chdir as cd

def build():
    input("\nЗверніть увагу що скріпт білдить програму для вашої ОС.\nНатисніть Enter щоб почати збірку...")

    print(f"\nЗбірка для {osname()}...\n")
    if sys.platform == "win32":
        cmd('python -m nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o pack-qt6-win --output-dir=../ --windows-icon-from-ico=../src/pack.ico --disable-console --deployment --company-name=xxanqw --product-name="Hudoliy ResourcePacker GUI for Windows (Qt6)" --file-version=0.0.2.2 --product-version=0.1.20.4 ../src/pack-qt6.py')
    elif sys.platform == "linux" or sys.platform == "linux2":
        cmd('python -m nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o pack-qt6-linux --output-dir=../ --disable-console --deployment ../src/pack-qt6.py')
    elif sys.platform == "darwin":
        cmd('python -m nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o pack-qt6-macos --output-dir=../ --disable-console --deployment ../src/pack-qt6.py')
    print(f"\nЗбірка для {osname()} завершена.\n")

def osname():
    if sys.platform == "win32":
        return "Windows"
    elif sys.platform == "linux" or sys.platform == "linux2":
        return "Linux"
    elif sys.platform == "darwin":
        return "macOS"

def main():
    current_directory = dir()
    current_directory_name = cdn(current_directory)
    print("Hudoliy ResourcePacker GUI builder\n==================================\n")

    expected_directory = "build"
    if current_directory_name != expected_directory:
        print("Ви запустили скрипт не з тієї папки, в якій він знаходиться.")
        if current_directory_name == "hudoliy-resourcepack":
            input("Оскільки ви знаходитесь в кореневій папці натисніть Enter аби змінити папку на build та запустити скріпт...")
            cd(expected_directory)
            build()
    else:
        build()

def cls():
    if sys.platform == "win32":
        cmd("cls")
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        cmd("clear")

if __name__ == "__main__":
    cls()
    main()