#! /bin/bash

echo "Запаковую.."
zip -qr pack.zip ./pack/*

echo "Знаходжу і записую SHA1 в файл.."
python3 ./src/mac/sha1.py

echo "Готово🫣"