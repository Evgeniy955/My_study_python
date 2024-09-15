words = ["apple", "banana", "avocado", "grape", "kiwi"]
new_task = []

def task_2():
    # for word in words:
    #     if word.startswith('a'):
    #         new_task.append(word.upper())
    [new_task.append(word.upper()) for word in words if word.startswith('a')]
    print(new_task)
    print("Count of words: ", len(new_task))
if __name__ == '__main__':
    task_2()