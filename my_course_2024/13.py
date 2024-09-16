original_set = {"apple", "banana", "cherry", "date", "fig"}
items_to_remove = ["banana", "date"]

def task_13():
    [original_set.remove(items_to_remove[word]) for word in range(len(items_to_remove))]
    return original_set

if __name__ == '__main__':
    print(task_13())