all_time = {'Given open WEB_STORE home page': 10212, "Then 'Pricing - Complete Anatomy' page is opened": 44,
            "When user clicks 'Login' button from store header": 3276, 'Then SSO window should be displayed': 4221,
            "When user enter email 'user_for_password_reset'": 2430, 'And click the next button': 2193,
            "And click 'Forgot your password' link": 2144,
            'And user enters email on reset password page and click reset password button': 4557,
            'And close login page': 3135, 'Then login on mail client and check reset password mail': 23694}


def milliseconds_to_hmsms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds, milliseconds


def all_time_json(all_time):
    for test_name, duration in all_time.items():
        hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(duration)
        print(
            f"Время выполнения теста {test_name}: {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")


def time_json_key(all_time):
    time_sum = 0
    for time in all_time.values():
        time_sum += time
    hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(time_sum)
    print(
        f"All time: Время выполнения тестов {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")


def time_ms(all_time):
    time_sum = 0
    for time in all_time.values():
        time_sum += time
    print(time_sum)


if __name__ == '__main__':
    time_ms(all_time)
    all_time_json(all_time)
    time_json_key(all_time)
