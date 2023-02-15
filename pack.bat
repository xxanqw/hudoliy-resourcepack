@echo off

echo Packing files...

cd 7zip
.\7za.exe a pack.zip ..\pack\* > NUL:
move pack.zip ..\ > NUL:

echo Done!
pause