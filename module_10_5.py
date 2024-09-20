import datetime
import multiprocessing
from multiprocessing import Pool


st = datetime.datetime.now()

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]


#Линейный вызов
for name in filenames:
    read_info(name)

# Многопроцессный
if __name__ == "__main__":
    with Pool(len(filenames)) as pool:
        res = pool.map(read_info, filenames)


end = datetime.datetime.now()
print(end - st)
