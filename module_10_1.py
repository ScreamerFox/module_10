from datetime import datetime
from time import sleep
from threading import Thread
import requests
import random

st_t = datetime.now()
name = 0


def wite_words(word_count, file_name):
    a = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        while a <= word_count:
            file.write(f'Какое-то слово № {a} \n')
            a += 1
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_t = datetime.now()
print(f'Вермя выполнения {end_t - st_t}')

st_t1 = datetime.now()

threads5 = Thread(target=wite_words, args=(10, 'example5.txt'))
threads6 = Thread(target=wite_words, args=(30, 'example6.txt'))
threads7 = Thread(target=wite_words, args=(200, 'example7.txt'))
threads8 = Thread(target=wite_words, args=(100, 'example8.txt'))

threads5.start()
threads6.start()
threads7.start()
threads8.start()
threads5.join()
threads6.join()
threads7.join()
threads8.join()


end_t1 = datetime.now()
print(f'Вермя выполнения {end_t1 - st_t1}')
