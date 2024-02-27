import json
from random_time import new_data
import os

file_path = "C:\\Users\\halitsyn.y\\PycharmProjects\\My_study_python\\2024\\add_elem_to_dict\\db.json"


def add_to_json(time):
    name_run = time.split(":")[0]
    run_time = time.split(" ")[1]
    json_data = {name_run: run_time}
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2)


def create_json(new_time):
    json_data = []
    if not os.path.exists(file_path):
        with open('db.json', 'w') as file:
            file.write(json.dumps(json_data))
    else:
        add_to_json(new_time)


create_json(new_data())
