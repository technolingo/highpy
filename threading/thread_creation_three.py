import threading as th


class MyThread:
    def __init__(self, number):
        self.number = number

    def even_numbers(self):
        if th.current_thread().getName() == 'Thread-1':
            for i in range(self.number):
                if i % 2 == 0:
                    print(i)
        else:
            print('Thread creation failed.')


obj = MyThread(10)
t = th.Thread(target=obj.even_numbers)
t.start()
