text = "apple banana apple orange banana apple orange apple"

def task_10():
    new_dict = {}
    text_list = list(text.split(' '))
    set_words = set(text_list)
    for item in range(len(set_words)):
        new_dict[list(set_words)[item]] = text_list.count(list(set_words)[item])
    print(new_dict)



if __name__ == '__main__':
    task_10()