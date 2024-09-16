number = 12345

def task_5():
    int_list = [int(i) for i in str(number)]
    sum_int = sum(int_list)
    multiplication = 1
    for i in int_list:
        multiplication *= i
    print("Sum: ", sum_int)
    print("Mult: ", multiplication)


if __name__ == '__main__':
    task_5()
