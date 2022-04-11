'''

In this we are passing an object of a given class as parameter
to function for utilisation or further processing.
In this context, we may employ static method to utilize it.
'''

class Emp:

    def __init__(self,eid,name='', sal=0.0):
        self.name = name
        self.sal = sal
        self.eid = eid

    def printEmployee(self):
        print('Employee name {} id {} & salary = {}'.format(self.name,self.eid,self.sal))


class Processing:
    def __init__(self):
        pass

    @staticmethod
    def processData(e):
        e.sal+=1200
        print('Modified : Employee name {} id {} & salary = {}'.format(e.name, e.eid, e.sal))


e = Emp(1234,'Ruskin',12000.45)
e.printEmployee()
p = Processing()
p.processData(e)
