'''
view vs copy methods

View method also creates a copy of the array but its an alias to it. That means,
any changes done to the original array will also change the copied array.

The copy method creates an altogether seperate copy of the array. That means,
any changes done to the original array will not change the copied array.
'''

from numpy import *

a = array([15,16,17,18,19])
#using view
b = a.view()
a[0] = 45
print(a)
print(b)

# using copy
c = a.copy()
a[1] = 1000
print(a)
print(c)

