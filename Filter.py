'''
Demonstration Of Filter Function
filter(conditional function, sequence)
'''

from array import *

a = [10,15,20,25,35,80,160,70,149]
q = filter((lambda x: x%2==0), a)
for i in q:
    print(i)