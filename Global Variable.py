x = 25
def bar():
    global x
    x = 30

    print("As of now x = ",x)
    print('calling function.....')
    print('After calling function, x = ',x)
bar()
print('Global x = ',x)

t = 'Hello \
my name is \
Abhijeet \
Banerjee'

print(t)
'''
In this case, the global variable value is being altered,
so inorder to preserve it, we should go for globals()[]
'''