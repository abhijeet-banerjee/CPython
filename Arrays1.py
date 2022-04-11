from array import *

ar = array('i',[15,54,78,96,123])
print(ar)

# creating another array
myarr = array(ar.typecode, [a**2 for a in ar])
print(myarr)
