from random import randint


def guess_number():
    number_rand = randint(1, 50)
    count = 0
    while count <= 6:
        number = int(input("Enter a number from 1 to 50: "))

        if number_rand > number:
            print("Your number is less")
        if number_rand < number:
            print("Your number is greater")
        if number_rand == number:
            print("Congratulations, you guessed right!")
        if number_rand != number and count == 6:
            print(f"Sorry you didn't guess. My number was: {number_rand}")
        count += 1


guess_number()
