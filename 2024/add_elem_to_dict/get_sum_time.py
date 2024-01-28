import json


def time_all_runs():
    get_all_time = 0
    with open('db.json') as f:
        data = json.load(f)
        print(data)
        for elem in data:
            for name, time in elem.items():
                get_all_time += int(time)
    return get_all_time


print(time_all_runs())