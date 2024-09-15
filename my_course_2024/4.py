word = "Ma da m"


def task_4():
    n = -1
    new_string = word.replace(" ", "").lower()
    # if word == word[::-1]:
    #     print('It"s palindrome')
    for i in new_string:
        if i != new_string[n]:
            print("It's not palindrome")
            break
        else:
            n -= 1
            if n < -len(new_string):
                print("It's palindrome")


if __name__ == '__main__':
    task_4()
