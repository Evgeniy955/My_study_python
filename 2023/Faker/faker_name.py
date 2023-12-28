from faker import Faker

name = str(Faker().name()).split(" ")[0]

print(name)