from os import system as cmd
import subprocess
import sys

print("Оновлюю..\n")
cmd("git pull")
if sys.platform == "win32":
    subprocess.Popen(['pack-qt6-win.exe'])
    sys.exit
elif sys.platform == "linux" or sys.platform == "linux2":
    subprocess.Popen(['pack-qt6-linux'])
    sys.exit
elif sys.platform == "darwin":
    subprocess.Popen(['pack-qt6-macos'])
    sys.exit
