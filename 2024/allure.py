import json
import os

import allure

# allure_report_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024/bc50efaf-d674-40a9-8abe-0a2743fbe662-result.json"  # Путь к Allure-отчету

folder_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024"
json_files = tuple(
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.split(".")[-1] == "json" and "categories" not in file
)


# # Получаем метаданные о времени выполнения теста
def get_all_test_durations(allure_report_path):
    # Загружаем содержимое Allure-отчета
    with open(allure_report_path, "r", encoding="utf-8") as file:
        allure_report = json.load(file)

    test_durations = {}  # Словарь для хранения времени выполнения каждого теста

    # Итерируем по результатам тестов в отчете
    for test_result in allure_report.get("steps", []):
        test_name = test_result.get("name")
        start_time = test_result.get("start")
        stop_time = test_result.get("stop")

        # Проверяем, что у теста есть имя и время начала/окончания
        if test_name and start_time and stop_time:
            duration = stop_time - start_time
            test_durations[test_name] = duration

    return test_durations

def time_for_json(allure_report_path):
    # Пример использования
    all_test_durations = get_all_test_durations(allure_report_path)

    # Выводим время выполнения для каждого теста
    for test_name, duration in all_test_durations.items():
        print(f"Время выполнения теста {test_name}: {duration} секунд")

if __name__ == '__main__':
    time_for_json(json_files)

