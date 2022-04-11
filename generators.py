'''
Simply generating even nos. inbetween the limit specified
'''

n = int(input('Enter a limit\n'))
def myfun():
    for i in range(2, (n + 1)):
        if i % 2 == 0:
            yield i

for j in myfun():
    print(j)


def myfun1():

    yield 'A'
    yield 'B'
    yield 'C'

f = myfun1()     # generator object
print(next(f))
print(next(f))
print(next(f))
