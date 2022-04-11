from threading import *
from time import  *

class Producer(object):
    def __init__(self):
        self.cv = Condition()
        self.l=[]

    def produceItems(self):
        self.cv.acquire()
        for x in range(1,11):
            self.l.append(x)
            print('Producing element %d' % x)
            sleep(2)
        else:
            print('Production Completed............')
            print('___________________________________________\n')
        self.cv.notify()
        self.cv.release()

class Consumer(Producer):
    def __init__ (self,ch):
        self.ch = ch

    def consumeItems(self):
        self.ch.cv.acquire()
        self.ch.cv.wait(timeout=0)
        lst = []
        for x in self.ch.l:
            lst.append(x**2)
            print('Consuming element %d' % x)
            sleep(2)
        else:
            print('Consumption Completed............')
            print('___________________________________________\n')
            for i in lst:
                print(i)
        self.ch.cv.release()


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produceItems)
t1.start()
t1.join()
t2 = Thread(target=c.consumeItems)
t2.start()
t2.join()

