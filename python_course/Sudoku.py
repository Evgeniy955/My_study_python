any = [[1, 2, 3], [9, 7, 8], [4, 5, 6]]


def any_duplicates(array):
    list = []
    for i in any:
        for y in i:
            if y in list:
                return True
            else:
                list.append(y)
    return False


print(any_duplicates(any))
