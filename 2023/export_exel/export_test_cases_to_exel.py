import xlsxwriter

filename = "/2023\\export_exel\\data_from_allure.txt"
workbook = xlsxwriter.Workbook('/2023\\export_exel\\my_data.xlsx')
sheet = workbook.add_worksheet()



data = [
    ['ID', 'Name']
]


def reading_file(filename):

    with open(filename, 'r') as file:
        read_lines = [line for line in file.readlines()]
        for test_case in read_lines:
            name_case = test_case.split('\n')
            data_row = name_case[0].split(" ", 1)
            if len(data_row) > 1:
                data.append([f"https://3d4medical.testrail.net/index.php?/cases/view/{data_row[0]}", data_row[1]])
            else:
                data.append([data_row[0]])

        return data


def export_to_exel():

    for row_idx, row_data in enumerate(reading_file(filename)):
        for col_idx, cell_data in enumerate(row_data):
            sheet.write(row_idx, col_idx, cell_data)

    workbook.close()

if __name__ == "__main__":
    export_to_exel()