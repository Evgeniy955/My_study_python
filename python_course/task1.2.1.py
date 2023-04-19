import io

word = 'eid: '
filename = 'yupdate-exec-yabrowser.log'
lis = list()


def reading_file(filename):
    with io.open(filename) as file:
        for line in reversed(file.readlines()):
            if word in line:
                split_line = line.split(word)
                lis.append(split_line[1])
                if len(lis) == 2:
                    break


def convert_to_dict(liss):
    return dict((k, int(v)) for k, v in (e.split('.') for e in liss.split(';')))


def difference():
    last = convert_to_dict(lis[0])
    prelast = convert_to_dict(lis[1])
    set_prelast = set(prelast.items())
    set_last = set(last.items())
    result_dict_orig = dict(set_last ^ set_prelast)
    [*result_dict] = dict(set_last ^ set_prelast)
    last_keys_dict = (result_dict[0], last.get(result_dict[0], "None"), result_dict[1], last.get(result_dict[1], "None"))
    prelast_keys_dict = (result_dict[0], prelast.get(result_dict[0], "None"), result_dict[1], prelast.get(result_dict[1], "None"))
    print("Предпоследние отличительные eid: ", prelast_keys_dict)
    print("Последние отличительные eid: ", last_keys_dict)
    return result_dict_orig


if __name__ == "__main__":
    reading_file(filename)
    print("Предпоследние eid: ", lis[1], end='')
    print("Последние eid: ", lis[0], end='')
    print(difference())
