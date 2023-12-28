import xlsxwriter

# Создание нового Excel файла
workbook = xlsxwriter.Workbook('путь_к_файлу.xlsx')
sheet = workbook.add_worksheet()

# Запись данных в ячейки (пример)
data = [
    ['Имя', 'Возраст', 'Зарплата'],
    ['Алиса', 25, 50000],
    ['Боб', 30, 60000],
    ['Клара', 22, 45000]
]

for row_idx, row_data in enumerate(data):
    for col_idx, cell_data in enumerate(row_data):
        sheet.write(row_idx, col_idx, cell_data)

# Закрытие и сохранение файла
workbook.close()

