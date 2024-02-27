import json

import allure

# Пример использования
test_step = "test_example"  # Замените на имя вашего теста
allure_report_path_1 = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024/bc50efaf-d674-40a9-8abe-0a2743fbe662-result.json"  # 55 секунд, 906 миллисекунд
allure_report_path_2 = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024/212458f1-7cbb-4722-8159-81ae802f95c8-result.json"  # 12sec 893 mil sec

allure_report_path = [allure_report_path_1, allure_report_path_2]
all_time = 0


def milliseconds_to_hmsms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds, milliseconds


# # Получаем метаданные о времени выполнения теста
def get_all_test_durations(allure_report_path):
    # Загружаем содержимое Allure-отчета
    with open(allure_report_path, "r", encoding="utf-8") as file:
        allure_report = json.load(file)
        print(allure_report.get("name"))

    test_durations = {}  # Словарь для хранения времени выполнения каждого теста

    # Итерируем по результатам тестов в отчете
    for test_result in allure_report.get("steps", []):
        test_step = test_result.get("name")
        start_time = test_result.get("start")
        stop_time = test_result.get("stop")

        # Проверяем, что у теста есть имя и время начала/окончания
        if test_step and start_time and stop_time:
            duration = stop_time - start_time
            test_durations[test_step] = duration

    return test_durations


'''Время одного словаря'''


def time_dict_json(elem_dict):
    for test_step, duration in elem_dict.items():
        hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(duration)
        print(
            f"Время выполнения теста {test_step}: {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")


'''Общее время'''


def time_json_key(elem_dict):
    time_sum = 0
    for time in elem_dict.values():
        if isinstance(time, int):
            time_sum += time
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_sum)
    print(
        f"All time: Время выполнения тестов {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")
    return time_sum


'''Получение информации о ранах'''


def get_info(allure_report_path, all_time):
    for path in allure_report_path:
        all_test_durations = get_all_test_durations(path)
        all_time += time_json_key(all_test_durations)
        time_dict_json(all_test_durations)
    return all_time


if __name__ == '__main__':
    print("json_files: ", len(allure_report_path))
    time_to_run = get_info(allure_report_path, all_time)
    print(time_to_run)
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_to_run)
    print(
        f"All time: Время выполнения тестов {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")
