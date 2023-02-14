#!/bin/sh

echo "Packing files..."

cd 7zip
chmod +x 7zz
7zz a pack.zip ../pack/ -bso0 -bsp0
mv pack.zip ../

echo "Done!"