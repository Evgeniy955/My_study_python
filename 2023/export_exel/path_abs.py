import os

from study_2023.Course.path_folder import ALLURE_REPORT_PATH


IS_NOT_REGRESS_PATH = os.environ.get("IS_NOT_REGRESS_PATH", os.path.dirname(__file__))

def f():
    print(os.path.dirname(__file__))
    print(ALLURE_REPORT_PATH)

if __name__ == '__main__':
    f()


'''# Полный путь к родительской папке
parent_folder = 'C:/путь/к/родительской_папке/'

# Создаем папку, если она не существует
folder_name = 'моя_папка'
folder_path = os.path.join(parent_folder, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Создаем новый Excel-файл в папке
file_path = os.path.join(folder_path, 'данные.xlsx')
workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()'''
