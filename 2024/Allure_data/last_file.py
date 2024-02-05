import os
from json import loads

folder_path = "/Users/halitsy.y/Downloads/App  IPAD tests results on 24.01.2024"


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
    passed = 0
    failed = 0
    names = []
    for json in (loads(open(file, "r").read()) for file in allure_report_path):
        if isinstance(json, dict):
            test_step = json.get("name")
            start_time = json.get("start")
            stop_time = json.get("stop")

            if test_step and start_time and stop_time:
                duration = stop_time - start_time
                all_time += duration

            if json.get("name") not in names:
                status = json.get("status")
                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                    names.append(json["name"])
    print(passed, failed, sep="\n")
    # return int(all_time)
    return int(all_time * 1.06)


if __name__ == '__main__':
    allure_report_path = get_file_paths(folder_path)
    time = get_test_execution_metadata(allure_report_path)
    print(time)
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time)
    print(
        f"\033[91m\033[1mTotal time: {int(hours)} hours, "
        f"{int(minutes)} minutes, {int(seconds)} seconds, {int(milliseconds)} milliseconds\033[0m"
    )
