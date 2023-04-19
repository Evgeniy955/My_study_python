from pytz import timezone
from datetime import datetime, timedelta


def time_zone(city_1, city_2):
    dt_format = "%d-%m-%Y %H:%M:%S"

    first_city = datetime.now(timezone(city_1))
    print(f'Date and time in {city_1}: \n', first_city.strftime(dt_format))

    sec_city = first_city.astimezone(timezone(city_2))
    print(f'Date and time in {city_2}: \n', sec_city.strftime(dt_format))

    def dif_time(first_time, sec_time):
        time_zone_1 = timedelta(hours=first_time.hour, minutes=first_time.minute, seconds=first_time.second)
        time_zone_2 = timedelta(hours=sec_time.hour, minutes=sec_time.minute, seconds=sec_time.second)
        dif_time_zone = time_zone_1 - time_zone_2
        print("Difference in time: ", abs(dif_time_zone))

    dif_time(first_city, sec_city)


if __name__ == "__main__":
    time_zone('Europe/Rome', 'Australia/Sydney')
