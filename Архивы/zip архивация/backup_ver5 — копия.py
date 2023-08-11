import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\My Documents', 'C:\\Code']
# Заметьте, что для имен, содержащих пробелы, необходимо использовать
# двойны кавычки.

# 2. Резервные копии должны хранится в основном каталоге резерва.
target_dir = 'E:\\Backup' # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: #проверяем введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# Создаем каталог, если его еще нет
if not os.path.exists(today):
    os.makedirs(today) # создает промежуточные папки в пути, если их там нет. И папку today
print('Каталог успешно создан', today)

try:
    zipp=zipfile.ZipFile(target, mode='w')# создание архива
    for path in source:
        print(path)
        for root, dirs, files in os.walk(path):# получаем адрес каталога и имена подкатологов и файлов
            for file in files:
                zipp.write(os.path.join(root,file))# пишем файлы в архив
    
    zipp.close()
    print('Резервная копия создана в D:\\backup_original')
except:
    print('Ошибка')
