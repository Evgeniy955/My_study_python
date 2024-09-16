set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

def task_12():
    if set1 == set2:
        print("The sets are identical")
    elif set1.issubset(set2):
        print("Set 1 - includes set 2")
    elif set2.issubset(set1):
        print("Set 2 - includes set 1")

if __name__ == '__main__':
    task_12()