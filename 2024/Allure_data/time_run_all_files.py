import json
import os

folder_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024"
all_time = 0


def get_file_paths(folder_path):
    json_files_path = tuple(
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.split(".")[-1] == "json" and "categories" not in file
    )
    return json_files_path


def milliseconds_to_hmsms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds, milliseconds


# Получаем метаданные о времени выполнения теста
def get_all_test_durations(allure_report_path):
    with open(allure_report_path, "r", encoding="utf-8") as file:
        allure_report = json.load(file)
        # print(allure_report.get("name"))

    test_durations = {}

    for test_result in allure_report.get("steps", []):
        test_step = test_result.get("name")
        start_time = test_result.get("start")
        stop_time = test_result.get("stop")

        if test_step and start_time and stop_time:
            duration = stop_time - start_time
            test_durations[test_step] = duration

    return test_durations


'''Общее время'''


def calculate_total_execution_time(elem_dict) -> int:
    time_sum = 0
    for time in elem_dict.values():
        if isinstance(time, int):
            time_sum += int(time * 1.06)

    '''hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_sum)'''
    # print(
    #     f"\033[91m\033[1mAll time: Время выполнения тестов {int(hours)} часов, "
    #     f"{int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд\033[0m"
    # )
    return time_sum


'''Получение информации о ранах'''


def get_info(allure_report_path, all_time):
    for path in allure_report_path:
        all_test_durations = get_all_test_durations(path)
        all_time += calculate_total_execution_time(all_test_durations)
    return all_time


if __name__ == '__main__':
    allure_report_path = get_file_paths(folder_path)
    # print("json_files: ", len(allure_report_path))
    time_to_run = get_info(allure_report_path, all_time)
    print(time_to_run)
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_to_run)
    print(
        f"\033[91m\033[1mAll time: Время выполнения тестов {int(hours)} часов, "
        f"{int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд\033[0m"
    )
