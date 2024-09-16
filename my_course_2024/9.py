shopping_lists = {
    "Alice": ["apple", "banana", "orange"],
    "Bob": ["banana", "milk", "orange"],
    "Charlie": ["apple", "milk", "bread"]
}


def task_9():
    new_dict = {}
    new_list = [elem for key in shopping_lists.values() for elem in key]
    only_names = set(new_list)
    for item in range(len(only_names)):
        new_dict[list(only_names)[item]] = new_list.count(list(only_names)[item])
    print(new_dict)


if __name__ == '__main__':
    task_9()

    # apple = 0
    # banana = 0
    # orange = 0
    # milk = 0
    # bread = 0
    # new_dict = {}
    # for key in shopping_lists.values():
    #     for elem in key:
    #         if elem == 'apple':
    #             apple += 1
    #             new_dict['apple'] = apple
    #         if elem == 'banana':
    #             banana += 1
    #             new_dict['banana'] = banana
    #         if elem == 'orange':
    #             orange += 1
    #             new_dict['orange'] = orange
    #         if elem == 'milk':
    #             milk += 1
    #             new_dict['milk'] = milk
    #         if elem == 'bread':
    #             bread += 1
    #             new_dict['bread'] = bread
