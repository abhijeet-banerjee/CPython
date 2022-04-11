class Father(object):

    def __init__(self,x):
        self.property = 80000
        self.x=x
        print('Fathers Total Property Share = ', self.property)
        print('Share for child is asking = ', self.x)

    def propertyDistribution(self):
        print('Property to be given = {}'.format(self.property-10000))


class Child(Father):

    def __init__(self,cld):
        super().__init__(cld)
        print('I am Child Calling')


c = Child(80000)
