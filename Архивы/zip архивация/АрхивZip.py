import zipfile
try:
    jungle_zip = zipfile.ZipFile('D:\\backup_original\\jungle.zip', 'w')
    jungle_zip.write('D:\\backup_original\\13-23_09_18.pdf', compress_type=zipfile.ZIP_DEFLATED)
    print('Архив создан')
    jungle_zip.close()
except:
    print('Ошибка')
