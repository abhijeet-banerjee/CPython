from threading import *
from time import *

'''
At a time a single person Ticket should be cut and 
that person only should be shown his seat.
'''

class Ticket:

    def __init__(self):
        pass

    def seat(self):
        name = current_thread().getName()

        print('Cut Ticket for %s' % name)
        sleep(4)
        print('Now Show Ticket for %20s' % name)


v = Ticket()
t1 = Thread(target=v.seat)
t2 = Thread(target=v.seat)
t3 = Thread(target=v.seat)
t4 = Thread(target=v.seat)
t1.setName("Ankur")
t2.setName("Sachin")
t3.setName("Anuradha")
t4.setName("Anjali")

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()




