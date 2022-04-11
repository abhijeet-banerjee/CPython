def mydecor(f):
    def inner():
        return f()+20
    return inner

def mydecor1(f):
    def inner():
        return f()*5
    return inner

def mydecor2(f):
    def inner():
        return f()*3
    return inner

@mydecor
@mydecor1
@mydecor2
def myval():
    return 10

f =myval()
print(f)


