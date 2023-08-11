import os
import zipfile


def create_zip_archive(source_folder, output_filename, output_path):
    with zipfile.ZipFile(os.path.join(output_path, output_filename), 'w') as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                arcname = os.path.relpath(file_path, source_folder)  # Относительный путь в архиве
                zipf.write(file_path, arcname)

source_folder = 'C:\\Users\\halitsyn.y\\Desktop\\backup_original\\Archive'
output_filename = 'Postman_English.zip'
output_path = '/study_2023/Course/Func'

create_zip_archive(source_folder, output_filename, output_path)