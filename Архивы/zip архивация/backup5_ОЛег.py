import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
sources = ['d:\\programming\\samples\\python\\3', 'd:\\programming\\samples\\python\\2']
# Заметьте, что для имен, содержащих пробелы, необходимо использовать
# двойны кавычки.

# 2. Резервные копии должны хранится в основном каталоге резерва.
target_dir = 'd:\\programming\\samples\\python\\backup' # Подставьте тот путь, который вы будете использовать.

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

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = ' '.join(sources)
print(zip_command)

zipp=zipfile.ZipFile(target, mode='w')# создание архива
for source in sources:
    print(source)
    for root, dirs, files in os.walk(source):# получаем адрес каталога и имена подкатологов и файлов
        for file in files:
            zipp.write(os.path.join(root,file))# пишем файлы в архив
        
zipp.close()

