
# Создание архива, запись файлов и директорий:

import os, zipfile

os.chdir('D:\\example')
print(os.listdir())

zipFile = zipfile.ZipFile('archive2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('readme.txt') # добавляем файл в архив[/grn]
zipFile.write('images') # добавляем (пустую) директорию в архив[/grn]
zipFile.write('images\\1.jpg')
zipFile.write('images\\2.jpg')
zipFile.close()

# Функция zipfile.is_zipfile() проверяет, является ли файл архивом или нет. Если да, то она вернет True, если нет — False.