'''
Assigning function to a variable
'''

def myfun(p):
    return (p**2)

a = myfun(15)
print(a)

'''
Function inside another function
'''

def fun():
    def msg():
        return "Hello"
    return msg
f = fun()
print(f()+ " Abhijeet")


'''
Passing function as parameter to another function
'''

def outer(f):
    return "Hey there "+f()
def mystr():
    return "Abhijeet"
z = outer(mystr)
print(z)
