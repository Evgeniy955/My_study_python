from datetime import date


def program():
    global zodiac_sign
    Year = input("year of birth:")
    Month = input("month of birth:")
    Day = input("day of birth:")
    Date_of_Birth = (Day + "/" + Month + "/" + Year)
    print('Your Date of Birth is ' + Date_of_Birth)
    d = date.today()
    y = d.year
    age = y - int(Year)
    if (int(Month) < int(d.month) or int(Day) > int(d.day)):
        age -= 1
        print('Your age is ' + str(age))
    else:
        print('Your age is ' + str(age))

    if ((int(Month) == 12 and int(Day) >= 22) or (int(Month) == 1 and int(Day) <= 19)):
        zodiac_sign = ("\n Capricorn")
    elif ((int(Month) == 1 and int(Day) >= 20) or (int(Month) == 2 and int(Day) <= 17)):
        zodiac_sign = ("\n aquarium")
    elif ((int(Month) == 2 and int(Day) >= 18) or (int(Month) == 3 and int(Day) <= 19)):
        zodiac_sign = ("\n Pices")
    elif ((int(Month) == 3 and int(Day) >= 20) or (int(Month) == 4 and int(Day) <= 19)):
        zodiac_sign = ("\n Aries")
    elif ((int(Month) == 4 and int(Day) >= 20) or (int(Month) == 5 and int(Day) <= 20)):
        zodiac_sign = ("\n Taurus")
    elif ((int(Month) == 5 and int(Day) >= 21) or (int(Month) == 6 and int(Day) <= 20)):
        zodiac_sign = ("\n Gemini")
    elif ((int(Month) == 6 and int(Day) >= 21) or (int(Month) == 7 and int(Day) <= 22)):
        zodiac_sign = ("\n Cancer")
    elif ((int(Month) == 7 and int(Day) >= 23) or (int(Month) == 8 and int(Day) <= 22)):
        zodiac_sign = ("\n Leo")
    elif ((int(Month) == 8 and int(Day) >= 23) or (int(Month) == 9 and int(Day) <= 22)):
        zodiac_sign = ("\n Virgo")
    elif ((int(Month) == 9 and int(Day) >= 23) or (int(Month) == 10 and int(Day) <= 22)):
        zodiac_sign = ("\n Libra")
    elif ((int(Month) == 10 and int(Day) >= 23) or (int(Month) == 11 and int(Day) <= 21)):
        zodiac_sign = ("\n Scorpio")
    elif ((int(Month) == 11 and int(Day) >= 22) or (int(Month) == 12 and int(Day) <= 21)):
        zodiac_sign = ("\n Sagittarius")

    print(zodiac_sign)

if __name__ == '__main__':
    program()
