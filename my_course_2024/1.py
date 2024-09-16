list1 = [5, 8, 12, 3, 9]
list2 = [7, 2, 10, 6, 4]
def task_1():
    new_list = list1 + list2
    final_list = sorted([num for num in new_list if num % 2 != 0])
    print(final_list)


if __name__ == '__main__':
    task_1()