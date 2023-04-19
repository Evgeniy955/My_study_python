class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)

print(mazda_car.name)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)

bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)

print(bmw_car.name)
print(bmw_car.year)
print(bmw_car.wheels_number)