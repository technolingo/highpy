import threading as th
import string
import time


def count_to_ten():
    print('Counting to ten...')
    for i in range(1, 11):
        time.sleep(0.5)
        print(i)


def first_five_letters():
    print('Enumerating letters...')
    for i in string.ascii_uppercase[:5]:
        time.sleep(1)
        print(i)


t1 = th.Thread(target=count_to_ten)
t2 = th.Thread(target=first_five_letters)
t1.start()
t2.start()
