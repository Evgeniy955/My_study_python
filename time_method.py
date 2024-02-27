import timeit

def first(time_func):
    while time_func != 0:
        print("Hello")
        x = 2*3*83-45+65/2
        print(x)
        time_func -=1

execution_time = timeit.timeit(lambda: first(10), number=1)

# Разбиваем время выполнения на секунды, миллисекунды и микросекунды
seconds = int(execution_time)
milliseconds = int((execution_time - seconds) * 1000)
microseconds = int((execution_time - seconds - milliseconds / 1000) * 1000000)

print("Время выполнения метода: {} секунд {} миллисекунд {} микросекунд".format(seconds, milliseconds, microseconds))
