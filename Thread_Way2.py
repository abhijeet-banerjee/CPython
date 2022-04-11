from threading import *
from time import sleep

class MyThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(5):
            print('i\'s value = ',i,' for Thread named ',current_thread().getName())
            sleep(2)


t = MyThread()
t.setName("LivQuick")
t.start()
t.join()

