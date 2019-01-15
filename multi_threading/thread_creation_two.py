import threading as th


class MyThread(th.Thread):
    def run(self):
        print(th.current_thread().getName())
        for i in range(5):
            for j in range(i + 1):
                print('*', end=' ')
            print('\r')


t = MyThread()
t.start()
