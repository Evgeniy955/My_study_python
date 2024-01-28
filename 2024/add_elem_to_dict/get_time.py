import json
from random_time import new_data
import os

file_path = "C:\\Users\\halitsyn.y\\PycharmProjects\\My_study_python\\2024\\add_elem_to_dict\\db.json"

# def get_run_time(time):
#     name_run = time.split(":")[0]
#     run_time = time.split(" ")[1]
#     to_json = {name_run: run_time}
#
#     with open('sw_templates.json', 'w') as f:
#         json.dump(to_json, f)
#
#     with open('sw_templates.json') as f:
#         print(f.read())
#
# get_run_time(new_data())

def create_json():
    json_data = []
    if not os.path.exists(file_path):
        with open('db.json', 'w') as file:
            file.write(json.dumps(json_data))


def add_to_json(time):
    name_run = time.split(":")[0]
    run_time = time.split(" ")[1]
    json_data = {name_run: run_time}
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

create_json()
add_to_json(new_data())