x = ['91.00.4472.114', '116.0.5845.92']

list_of_numbers = []
for _ in x:
    list_of_numbers.append(int(_.split(".")[0]))


print(str(max(list_of_numbers)))