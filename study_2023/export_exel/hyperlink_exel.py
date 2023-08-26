import os
import xlsxwriter

from study_2023.Course.path_folder import ALLURE_REPORT_PATH
from study_2023.export_exel.path_abs import IS_NOT_REGRESS_PATH


file_name = 'data_from_allure.txt'

# Формируем полный путь к файлу
filename = os.path.join(IS_NOT_REGRESS_PATH, file_name)

# Ваши данные (пример)
data = {
    'ID': [],
    'Name': [],
    'Link': []
}


# Создаем папку, если она не существует
folder_name = 'results'
folder_path = os.path.join(ALLURE_REPORT_PATH, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Создаем новый Excel-файл в папке
file_path = os.path.join(folder_path, 'link_data_new.xlsx')
workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()

# # Создаем новый Excel-файл
# workbook = xlsxwriter.Workbook('C:\\Users\\halitsyn.y\\PycharmProjects\\My_study_python\\study_2023\\export_exel\\link_data_new.xlsx')
# worksheet = workbook.add_worksheet()

def reading_file(filename):

    with open(filename, 'r') as file:
        read_lines = [line for line in file.readlines()]
        for test_case in read_lines:
            name_case = test_case.split('\n')
            data_row = name_case[0].split(" ", 1)
            if len(data_row) > 1:
                data['ID'].append(data_row[0])
                data['Name'].append(data_row[1])
                data['Link'].append(f"https://3d4medical.testrail.net/index.php?/cases/view/{data_row[0]}")
            # else:
            #     data.append([data_row[0]])

        return data

def export_to_exel():
    # Добавляем заголовки в таблицу Excel
    header_format = workbook.add_format({'bold': True, 'underline': True, 'align': 'center'})
    for col_num, header in enumerate(reading_file(filename).keys()):
        worksheet.write(0, col_num, header, header_format)

    # Добавляем данные и гиперссылки в таблицу Excel
    url_format = workbook.add_format({'color': 'blue', 'underline': True})
    for row_num, (id, name, link) in enumerate(zip(data['ID'], data['Name'], data['Link']), 1):
        worksheet.write(row_num, 0, id)
        worksheet.write_url(row_num, 2, link, url_format, string='Link to TestRail')
        worksheet.write(row_num, 1, name)

    # Сохраняем Excel-файл
    workbook.close()


if __name__ == "__main__":
    export_to_exel()


