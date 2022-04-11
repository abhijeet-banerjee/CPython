from abc import  *

'''
Python has no explicit concept for Interfaces
An Interface when written in Python should only contain all of the abstract methods
only, by its defination

'''
class MyAbstractClass(ABC):

    def __init__(self):
        self.myvar = 145 # No subclass of this Abstract Class can use it, and
                         # solely belongs to Abstract class only.

    @abstractmethod
    def calculate(self):
        pass

    def mychoice(self):
        print('This is just a concrete method demonstration')



class Square(MyAbstractClass):

    def __init__(self,x):
        self.x = x

    def calculate(self):
        return (self.x * self.x)


class Rectangle(MyAbstractClass):

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def calculate(self):
        return (self.x * self.y)

# create objects to the sub-classes

s = Square(55)
print(s.calculate())
s.mychoice()
r = Rectangle(77,99)
print(r.calculate())
r.mychoice()