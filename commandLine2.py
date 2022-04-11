from argparse import *

a = ArgumentParser('description = This Program multiplies all the arguments together')
a.add_argument('nums', nargs='*')
v = a.parse_args()
s = 1
for i in v.nums:
    s *= int(i)

else:
    print('Product is %d' % s)




