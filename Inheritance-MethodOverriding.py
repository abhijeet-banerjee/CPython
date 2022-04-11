class Father(object):

    def __init__(self):
        self.property = 80000
        print('Fathers Total Property Share = ', self.property)

    def propertyDistribution(self):
        print('Property to be given = {}'.format(self.property-10000))


class Child(Father):

    def __init__(self):
        self.property = 80000
        print('Fathers Total Property Share = ',self.property)

    def propertyDistribution(self):
        print('Property to be given = {}'.format(self.property))

c = Child()
c.propertyDistribution()
