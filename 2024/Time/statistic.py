import json
import os
from json import loads

folder_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024"



json_files = tuple(
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.split(".")[-1] == "json" and "categories" not in file
)

def get_statistic(json_files):
    passed = 0
    failed = 0
    names = []
    for file in (loads(open(file, "r").read()) for file in json_files):
        if file.get("name") not in names:
            status = file.get("status")
            if status == "passed":
                passed += 1
            elif status == "failed":
                failed += 1
            names.append(file["name"])
    print(passed, failed, sep="\n")

def get_all_test_durations(json_files):
    # Загружаем содержимое Allure-отчета
    for json in json_files:
        with open(json, "r", encoding="utf-8") as file:
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

if __name__ == '__main__':
    get_statistic(json_files)
    print(get_all_test_durations(json_files))