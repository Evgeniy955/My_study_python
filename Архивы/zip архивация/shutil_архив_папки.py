import shutil, os


target_path = 'C:\\Users\\Yevhen\\Desktop\\backup_original\\Archive' # root_dir - это каталог, который будет корневым каталогом архива;
# например, мы обычно запускаем chdir в root_dir перед созданием архива.
file_to_zip = r'new' # base_dir - это каталог, откуда мы начинаем архивирование; (папка, котоорая будет заархивированная)
# то есть base_dir будет общим префиксом всех файлов и каталогов в архиве.
try:
    shutil.make_archive('C:\\Users\\Yevhen\\Documents\\Archives\\archive2', 'zip', target_path, file_to_zip)
except:
    print('pass')


# shutil.make_archive( base_name , format [ , root_dir [ , base_dir ] ] ) 
# base_name - это имя файла для создания, включая путь, за вычетом любого расширения, зависящего от формата.
# format является форматом архива: один из «zip» (если zlibмодуль доступен), «tar», «gztar» (если zlibмодуль доступен),
# «bztar» (если bz2модуль доступен) или «xztar» ( если lzmaмодуль доступен).