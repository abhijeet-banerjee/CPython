from threading import *
from time import sleep

class MyThread:

    def __init__(self):
        pass

    def exec(self,x):
        for i in range(x):
            print('i\'s value = ',i,' for Thread named ',current_thread().getName())
            sleep(2)

n = MyThread()
t = Thread(target=n.exec(7,))
t.setName('LivQuick')
t.start()
t.join()