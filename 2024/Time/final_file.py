import json

import allure

allure_report_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024/bc50efaf-d674-40a9-8abe-0a2743fbe662-result.json"


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


def milliseconds_to_hmsms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds, milliseconds


def all_time_json(all_time):
    for test_name, duration in all_time.items():
        hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(duration)
        print(
            f"Время выполнения теста {test_name}: {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")


def time_json_key(all_time):
    time_sum = 0
    for time in all_time.values():
        time_sum += time
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_sum)
    print(
        f"All time: Время выполнения тестов {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")


def time_ms(all_time):
    time_sum = 0
    for time in all_time.values():
        time_sum += time
    print(time_sum)


if __name__ == '__main__':
    test_durations = get_all_test_durations(allure_report_path)
    time_ms(test_durations)
    all_time_json(test_durations)
    time_json_key(test_durations)
