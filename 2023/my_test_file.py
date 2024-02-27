my_list = ["apple", "cherry", "date"]

word_to_remove = "banana"
if word_to_remove in my_list:
    my_list.remove(word_to_remove)
else:
    print(f"{word_to_remove} не найдено в списке.")

print(my_list)
