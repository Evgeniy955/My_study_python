import os
import zipfile
       
jungle_zip = zipfile.ZipFile('D:\\backup_original\\jungle.zip', 'w', zipfile.ZIP_DEFLATED)

path = 'C:\\Code'
  
for root, dirs, files in os.walk(path):
    for file in files:
        jungle_zip.write(os.path.join(root, file)) 
jungle_zip.close()
if not jungle_zip:
    print('Создание резервной копии НЕ УДАЛОСЬ')
else:
    print('Резервная копия успешно создана в D:\\backup_original')
