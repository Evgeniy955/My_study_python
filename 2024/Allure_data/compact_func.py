import os
from json import loads

folder_path = "/Users/halitsy.y/Downloads/Web  None tests results on 10.01.2024"


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
def get_test_execution_metadata(allure_report_path):
    all_time = 0
    for json in (loads(open(file, "r").read()) for file in allure_report_path):
        for step in json["steps"]:
            test_step = step.get("name")
            start_time = step.get("start")
            stop_time = step.get("stop")

            if test_step and start_time and stop_time:
                duration = stop_time - start_time
                all_time += duration
    return int(all_time * 1.06)


if __name__ == '__main__':
    allure_report_path = get_file_paths(folder_path)
    time = get_test_execution_metadata(allure_report_path)
    print(time)
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time)
    print(
        f"\033[91m\033[1mAll time: Время выполнения тестов {int(hours)} часов, "
        f"{int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд\033[0m"
    )
