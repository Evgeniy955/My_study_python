
# Получение информации о содержимом zip-архива:

import os, zipfile
os.chdir('D:\\example')
zipFile = zipfile.ZipFile('archive2.zip', 'r')
zipFile.extract('readme.txt') # извлекаем отдельный файл из корня архива 
# \\example\\readme.txt'
zipFile.extract('images/1.jpg') # извлекаем отдельный файл из директории images
# \\example\\images\\1.jpg'
zipFile.extractall() # извлекаем весь архив в текущую директорию[/grn]
zipFile.extractall('archive') # извлекаем весь архив в директорию archive[/grn]
zipFile.close()
