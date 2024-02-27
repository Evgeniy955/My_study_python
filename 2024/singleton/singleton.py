# Паттерны или шаблоны разработки - это общие способы решения частых задач и проблемм
# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию, объект всегда один
# Monostate - это шаблон предоставления глобального доступа к состоянию, объекты могут быть разными
# нужен для одной точки доступа к ресурсам/данным и для того чтобы ресурсоемкие задачи сделать 1 раз
# плюсы: 1 раз выполняем тяжелые задачи, имеет 1 вход для всей системы
# минусы: общесистемная глобальная переменная
# Модуль в Python - это синглтон

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print("Do some hard work")
        # parse, db, work with data/resourses ect...
        self.data = 101


# class Monostate:
#     _share_state = {}
#
#     def __init__(self):
#         self.__dict__ = self.__dict__
#         if not self._share_state:
#             print("Do some hard work")
#             # parse, db, work with data/resourses ect...
#             self.data = 101


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)
    print(Singleton())
