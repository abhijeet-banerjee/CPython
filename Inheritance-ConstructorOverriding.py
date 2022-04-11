class Father(object):

    def __init__(self):
        self.property = 80000
        print('Fathers Property Share = ',self.property)

class Child(Father):

    def __init__(self):
        self.property = 90000
        print('Fathers Property Share = ',self.property)


c = Child()

