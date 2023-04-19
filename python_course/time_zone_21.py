from pytz import timezone
from datetime import datetime, timedelta

server_time = datetime.now()
print("Local time: ", server_time.strftime("%m-%d-%Y %H:%M:%S"))


def first_time_zone(city_1):
    first_city = timezone(city_1).fromutc(server_time)
    print(f'Date and time in {city_1}: \n', first_city.strftime("%m-%d-%Y %H:%M:%S"))
    return first_city


def sec_time_zone(city_2):
    sec_city = timezone(city_2).fromutc(server_time)
    print(f'Date and time in {city_2}: \n', sec_city.strftime("%m-%d-%Y %H:%M:%S"))
    return sec_city


def dif_time(first_time, sec_time):
    time_zone_1 = timedelta(hours=first_time.hour, minutes=first_time.minute, seconds=first_time.second)
    time_zone_2 = timedelta(hours=sec_time.hour, minutes=sec_time.minute, seconds=sec_time.second)
    dif_time_zone = time_zone_1 - time_zone_2
    print("Difference in time: ", abs(dif_time_zone))


if __name__ == "__main__":
    tz_1 = first_time_zone('America/Los_Angeles')
    tz_2 = sec_time_zone('Asia/Dubai')
    dif_time(tz_1, tz_2)
