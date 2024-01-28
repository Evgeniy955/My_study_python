import json


def time_all_runs():
    get_all_time = 0
    with open('db.json') as f:
        data = json.load(f)
        for elem in data:
            for time in elem.values():
                get_all_time += int(time)
    return get_all_time


def seconds_to_hms(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds


def result_time():
    hours, minutes, seconds = seconds_to_hms(time_all_runs())
    print(f"Run times: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")


if __name__ == '__main__':
    result_time()
