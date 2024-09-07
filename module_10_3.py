import time
from datetime import datetime
from threading import Thread
import threading
import requests
import random

st_t = datetime.now()

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def str(self):
        return self.balance

    def deposit(self):
        for i in range(1000):
            dep = random.randint(50, 500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(1000):
            take_s = random.randint(50, 500)
            print(f'Запрос на снятие {take_s}')
            if take_s <= self.balance:
                self.balance -= take_s
                print(f'Снятие - {take_s}, баланс - {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств на счёте!')
                self.lock.acquire()
            time.sleep(0.001)


try:
    bk = Bank()

    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
finally:
    print(f'Итоговый баланс - {bk.str()}')


end_t = datetime.now()
print(f'Вермя выполнения {end_t - st_t}')
