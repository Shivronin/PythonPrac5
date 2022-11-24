import multiprocessing 
import os
from datetime import datetime

def producer (que):
    while True:
        if que.empty():
            continue
        a = que.get()
        b = que.get()
        digit = a ** b
        s = 0
        for i in range(digit+1):
            s += i
        my_file = r"./result.txt"
        with open( my_file,  'a') as file:
            now = datetime.now()
            date_format = "{}.{}.{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)
            file.write(f"{date_format} {a}^{b}={digit} {s}\n")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    proProcess = multiprocessing.Process(target = producer, args=(queue,))
    proProcess.start()
    while True:
        print("Введите число")
        x = int(input())
        print("Введите степень числа")
        y = int(input())
        queue.put(x)
        queue.put(y)     

    