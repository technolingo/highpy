import threading as th


if th.current_thread() == th.main_thread():
    print('Main thread')
else:
    print('Non-main thread')


def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)


def odd_numbers(n):
    for i in range(n):
        if i % 2 != 0:
            print(i)


te = th.Thread(target=even_numbers(10), name="EvenThread")
te.start()

to = th.Thread(target=odd_numbers(10), name="OddThread")
to.start()
