
a = 145
def myfun():
    a = 74
    globals()['a'] = globals()['a'] + 1
    print("Local variable ",a)


myfun()
print("Global variable ",a)

'''
We can use the global keyword fore only accessing the global variable
Using globals()['a'] we can directly access the global variable namespace without
affecting function's local variable value
'''