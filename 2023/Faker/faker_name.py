from faker import Faker

name = str(Faker().name())
first_name = name.split(" ")[0]
word = Faker().word()

print(first_name, word)