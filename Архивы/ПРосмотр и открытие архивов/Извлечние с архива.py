
# Получение информации о содержимом zip-архива:

import os, zipfile
os.chdir('D:\\example')
zipFile = zipfile.ZipFile('archive2.zip', 'r')
zipFile.extract('readme.txt') # извлекаем отдельный файл из корня архива 
# \\example\\readme.txt'
zipFile.extract('images/1.jpg') # извлекаем отдельный файл из директории images
# \\example\\images\\1.jpg'
with zipfile.ZipFile("archive2.zip","r") as zip_ref:
    zip_ref.extractall() # извлекаем весь архив в текущую директорию zip
with zipfile.ZipFile("archive2.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")  # извлекаем весь архив в директорию targetdir
zipFile.close()
