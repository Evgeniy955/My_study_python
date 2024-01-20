def milliseconds_to_hmsms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds, milliseconds

# Пример использования
total_milliseconds = 45321566  # Замените на количество миллисекунд, которое вы хотите преобразовать
hours, minutes, seconds, milliseconds = milliseconds_to_hmsms(total_milliseconds)

print(f"{int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд, {int(milliseconds)} миллисекунд")
