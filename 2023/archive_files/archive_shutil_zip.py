import os
import shutil

def create_zip_archive(source_folder, output_filename, output_path):
    shutil.make_archive(os.path.join(output_path, output_filename), 'zip', source_folder)

source_folder = 'C:\\Users\\halitsyn.y\\Desktop\\backup_original\\Archive'
output_filename = 'Postman_English'
output_path = '/2023/Course/Func'

create_zip_archive(source_folder, output_filename, output_path)
