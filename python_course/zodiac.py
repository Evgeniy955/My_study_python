from datetime import date


def year_dob(year):
    return 1900 < year < 2022


def month_dob(month):
    return 1 <= month <= 12


def day_dob(y, m, date_ob):
    return date(y, m, date_ob)


def dob(ymd):
    global year_1, month_1
    while True:
        try:
            date_of_birthday = abs(int(input(ymd)))
            if ymd == "Year of birth: ":
                if not year_dob(date_of_birthday):
                    print('Enter the correct year of birth')
                    continue
                else:
                    year_1 = date_of_birthday
            elif ymd == "Month of birth: ":
                if not month_dob(date_of_birthday):
                    print('Enter the correct month')
                    continue
                else:
                    month_1 = date_of_birthday
            elif ymd == "Day of birth: ":
                if not day_dob(year_1, month_1, date_of_birthday):
                    print('Enter the correct date')
                    continue
        except ValueError:
            print('Enter valid birth date')
        else:
            return date_of_birthday


def zodiac():
    global zodiac_sign
    year = dob("Year of birth: ")
    month = dob("Month of birth: ")
    day = dob("Day of birth: ")
    date_of_Birth = f'{day}/{month}/{year}'
    print('\nYour Date of Birth is ' + date_of_Birth)
    d = date.today()
    y = d.year
    age = y - int(year)
    if month > d.month or month == d.month and day > d.day:
        age -= 1
    print(f'Your age is {age}')

    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = ("Capricorn")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 17):
        zodiac_sign = ("Aquarium")
    elif (month == 2 and day >= 18) or (month == 3 and day <= 19):
        zodiac_sign = ("Pices")
    elif (month == 3 and day >= 20) or (month == 4 and day <= 19):
        zodiac_sign = ("Aries")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = ("Taurus")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = ("Gemini")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = ("Cancer")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = ("Leo")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = ("Virgo")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = ("Libra")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = ("Scorpio")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Sagittarius"

    return f'Your zodiac sign: {zodiac_sign}'


if __name__ == "__main__":
    print(zodiac())
