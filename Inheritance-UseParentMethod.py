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
        self.cld = cld
        super().__init__(cld)
        print('I am Child Calling')

    def propertyDistribution(self):
        print('Property finally accalimed for = {}'.format(self.cld))


c = Child(80000)
c.propertyDistribution()