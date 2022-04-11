'''
Demonstration of Private variable and its
resolution using Name Mangling method
'''

class Demo(object):
    def __init__(self):
        self.__y = 120

    def display(self):
        print('Private Variable y = %d' % self.__y)


# outside of the class private variable is not available
v = Demo()
print(v.__y)

# Using Name Mangling we can still use the class private variable
print(v._Demo__y)