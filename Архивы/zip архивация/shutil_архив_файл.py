import shutil, os


target_path = 'D:\\backup_original' # root_dir - это каталог, который будет корневым каталогом архива;
# например, мы обычно запускаем chdir в root_dir перед созданием архива.
file_to_zip = 'D:\\backup_original\\Archive\\test.txt' # base_dir - это каталог, откуда мы начинаем архивирование;
# то есть base_dir будет общим префиксом всех файлов и каталогов в архиве.
try:
    shutil.make_archive('D:\\backup_original\\Archive\\archive', 'zip', target_path, file_to_zip)
except:
    pass

# shutil.make_archive( base_name , format [ , root_dir [ , base_dir ] ] ) 
# base_name - это имя файла для создания, включая путь, за вычетом любого расширения, зависящего от формата.
# format является форматом архива: один из «zip» (если zlibмодуль доступен), «tar», «gztar» (если zlibмодуль доступен),
# «bztar» (если bz2модуль доступен) или «xztar» ( если lzmaмодуль доступен).