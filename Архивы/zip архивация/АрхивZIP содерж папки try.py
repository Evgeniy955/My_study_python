import os
import zipfile
try:
    jungle_zip = zipfile.ZipFile('D:\\backup_original\\jungle.zip', 'w', zipfile.ZIP_DEFLATED)

    path = 'C:\\Code'
  
    for root, dirs, files in os.walk(path):
        for file in files:
            jungle_zip.write(os.path.join(root, file))
            print('Резервная копия создана в D:\\backup_original')
            jungle_zip.close()
except:
    print('Ошибка')
