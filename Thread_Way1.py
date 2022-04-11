from threading import *

def mythread_demo(x):
    for i in range(x):
        print('Thread named {}  iterated for i = {}'.format(current_thread().getName(),i))

t = Thread(target=mythread_demo,args=(7,))
t.setName('LivQuick')
t.start()
t.join()