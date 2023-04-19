from datetime import date

list_friday_13 = []
date_today = date.today()
year = date_today.year


def ten_fridays_13(y):
    while len(list_friday_13) < 10:
        [list_friday_13.append(date(y, m, 13)) for m in range(1, 13) if
         date(y, m, 13).isoweekday() == 5 and date(y, m, 13) > date_today]
        y += 1

    [print(i) for i in list_friday_13]


if __name__ == "__main__":
    ten_fridays_13(year)
