class Father(object):

    def __init__(self):
        self.property = 80000
        print('Fathers Property = ',self.property)

class Child(Father):
    pass

c = Child()

