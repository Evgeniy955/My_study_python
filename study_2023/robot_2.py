from colorama import init, Fore, Style
import time
import sys

# Инициализация colorama
init(autoreset=True)

class RobotBase:
    def __init__(self, name):
        self.name = name
        print(Fore.CYAN + f"[Создание] Робот {self.name} готов к работе.")
        self.beep()

    def status(self):
        print(Fore.YELLOW + f"Робот {self.name}: Статус неизвестен.")

    def beep(self):
        print('\a', end='')  # системный бип


class RobotLauncher(RobotBase):
    def launch(self):
        print(Fore.GREEN + f"[Запуск] Робот {self.name} вышел на задание.")
        self.status()
        self.beep()

    def status(self):
        print(Fore.BLUE + f"Робот {self.name}: В активной фазе выполнения задания.")
        self.beep()


class RobotDecommissioner(RobotLauncher):
    def shutdown(self):
        print(Fore.RED + f"[Завершение] Робот {self.name} завершает работу.")
        self.status()
        self.beep()

    def status(self):
        print(Fore.MAGENTA + f"Робот {self.name}: Выведен из эксплуатации. До свидания!")
        self.beep()





if __name__ == "__main__":
    robot = RobotDecommissioner("R2-D2")
    time.sleep(0.5)
    robot.launch()
    time.sleep(0.5)
    robot.shutdown()