from pytz import timezone
from datetime import datetime, timedelta

dt_format = "%m-%d-%Y %H:%M:%S"


def first_time_zone(city_1):
    first_city = datetime.now(timezone(city_1))
    print(f'Date and time in {city_1}: \n', first_city.strftime(dt_format))
    return first_city


def sec_time_zone(city_2):
    sec_city = datetime.now(timezone(city_2))
    print(f'Date and time in {city_2}: \n', sec_city.strftime(dt_format))
    return sec_city


def dif_time(first_time, sec_time):
    time_zone_1 = timedelta(hours=first_time.hour, minutes=first_time.minute, seconds=first_time.second)
    time_zone_2 = timedelta(hours=sec_time.hour, minutes=sec_time.minute, seconds=sec_time.second)
    dif_time_zone = time_zone_1 - time_zone_2
    print("Difference in time: ", abs(dif_time_zone))


if __name__ == "__main__":
    tz_1 = first_time_zone('Europe/Rome')
    tz_2 = sec_time_zone('Australia/Sydney')
    dif_time(tz_1, tz_2)
