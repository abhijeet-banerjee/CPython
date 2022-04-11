from numpy import *
# reshaping a given array

ar = [1,2,3,4,5,6,7,8,9,10,11,12]
c = reshape(ar,(2,2,3))
print(c)
print(c.nbytes)
print(c.itemsize)