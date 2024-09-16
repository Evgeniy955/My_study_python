num = 5.6789


def task_6():
    new_number = round(num, 2)
    int_number = round(new_number)
    part_int = str(num).split('.')
    int_part, float_part = int(part_int[0]), int(part_int[1])
    print(new_number)
    print(int_number)
    print(int_part)
    print(float_part)

if __name__ == '__main__':
    task_6()