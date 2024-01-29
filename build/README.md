## Windows/Linux/MacOS
 - Мати встановлений Python [3.11.6](https://www.python.org/downloads/release/python-3116/#:~:text=Python%20community.-,Files,-Version)
 - Встановити залежності `pip` або `pip3 install -r requirements.pip`
 - Для лінукса встановити `patchelf` та `ccache`
```
   Arch
   sudo pacman -S patchelf ccache
   yay -S patchelf ccache

   Debian/Ubuntu
   sudo apt install patchelf ccache
```
 - Запустити скріпт `python` або `python3 build.py`  
 (ВАЖЛИВО запускати скріпт саме з цієї папки)