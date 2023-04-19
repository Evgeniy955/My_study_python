x = "D:TUpdaterController::SetUniqueParam(429): eid:"
filename = 'yupdate-exec-yabrowser.log'
list_dict = list()


def reading_file(filename):
    with open(filename, 'r') as file:
        lines_par = [line for line in file.readlines()[::-1] if x in line]

    def part(last_part, prelast_part):
        part_data_1 = prelast_part.split(" ")
        part_data_2 = last_part.split(" ")
        part_keys_1 = part_data_1[3].split(";")
        part_keys_2 = part_data_2[3].split(";")
        list_dict.append(part_keys_1)
        list_dict.append(part_keys_2)
        print("Last eid: " + part_data_2[3], "Penultimate eid: " + part_data_1[3])

    part(lines_par[0], lines_par[1])


def convert_dict(part_keys):
    return dict(zip([i[:3] for i in part_keys], [i[-1] for i in part_keys]))


def difference():
    global del_elem
    prelast = convert_dict(list_dict[0])
    last = convert_dict(list_dict[1])

    update_dict = {}
    update_dict_prelast = {}
    update_dict_last = {}

    for i, v in prelast.items():
        if i in last.keys() and prelast[i] != last[i]:
            update_dict[i] = prelast[i], last[i]
            update_dict_prelast[i] = prelast[i]
            update_dict_last[i] = last[i]
        elif i not in last.keys():
            update_dict[i] = prelast[i], None
            update_dict_prelast[i] = prelast[i]
            del_elem = f'Item has been removed "{i}: {prelast[i]}", '
    for k in last.keys():
        if k not in prelast.keys():
            update_dict[k] = last[k]

    print("Prelast_item: ", update_dict_prelast)
    print(f'last_item: {str(del_elem)}', update_dict_last)
    print("Differences: ", update_dict)


if __name__ == "__main__":
    reading_file(filename)
    difference()
