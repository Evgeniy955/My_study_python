import shutil, os


target_path = 'D:\\backup_original\\Archive3' # папка, куда распаковывается. Создается сама

try:
    shutil.unpack_archive('D:\\backup_original\\archive2.zip', target_path, 'zip')
except:
    print('pass')


# shutil.unpack_archive( имя файла [ , extract_dir [ , формат ] ] ) 
# Распакуйте архив. filename - полный путь к архиву
# extract_dir - имя целевого каталога, в который распаковывается архив. Если не указан, используется текущий рабочий каталог.
# формат - это формат архива: один из «zip», «tar», «gztar», «bztar» или «xztar». Или любой другой формат,
# зарегистрированный в register_unpack_format(). Если не указан, unpack_archive() будет использовать расширение имени файла архива
# и посмотреть, был ли распаковщик зарегистрирован для этого расширения. Если ничего не найдено, a ValueErrorподнимается.