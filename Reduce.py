'''
Demonstration Of Filter Function
filter(function, sequence)
'''
from functools import *

a = [10,20,30,40,55]
x = reduce((lambda x,y: x*y), a)
print(x)
