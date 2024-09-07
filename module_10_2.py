import time
from datetime import datetime
from threading import Thread
import threading


st_t = datetime.now()

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        day = 0
        while enemy > 0:
            print(f'{self.name}, На нас напали!')
            enemy -= self.power
            day += 1
            print(f'{self.name} сражается {day} дней, осталось {enemy} Врагов')
            time.sleep(1)
        else:
            print(f'{self.name} одержал победу за {day} дня(дней)!')




# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


# Вывод строки об окончании сражения


end_t = datetime.now()
print(f'Вермя выполнения {end_t - st_t}')


