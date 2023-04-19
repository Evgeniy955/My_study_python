from datetime import date

list_friday_13 = []
date_today = date.today()
year = date_today.year


def ten_fridays_13(y):
    while len(list_friday_13) < 10:
        for m in range(1, 13):
            if date(y, m, 13).isoweekday() == 5 and date(y, m, 13) > date_today:
                list_friday_13.append(date(y, m, 13))
            if m == 12:
                y += 1
    return [print(i) for i in list_friday_13]


if __name__ == "__main__":
    ten_fridays_13(year)

