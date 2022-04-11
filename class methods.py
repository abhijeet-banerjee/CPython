'''
class methods are those methods which act on class variables
'''

class Demo:

    @classmethod
    def myclsmethod(cls,p):
        p+=1
        print('The value of variable "p" %d' % p)

    def __init__(self):
        pass

Demo.myclsmethod(1001)