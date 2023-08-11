
# Получение информации о содержимом zip-архива:

import os, zipfile
os.chdir('D:\\example')
zipFile = zipfile.ZipFile('archive2.zip', 'r')
print(zipFile.namelist()) # получаем информацию о файлах и директориях. Как прочитать содержимое архива zipFile.printdir()
zipInfo = zipFile.getinfo('readme.txt') # получаем информацию об отдельном файле
# print(zipFile.getinfo('readme.txt'))
print('file_size', zipInfo.file_size) # обычный размер
# zipInfo.file_size
print('compress_size', zipInfo.compress_size) # сжатый размер
# zipInfo.compress_size
zipFile.close()