'''
    Inheritance Chaining
'''
class X(object):
    def __init__(self):
        print('I am constructor for class X')


class Y(X):
    def __init__(self):
        super().__init__()
        print('I am constructor for class Y')


class Z(X):
    def __init__(self):
        super().__init__()
        print('I am constructor for class Z')

class P(X):
    def __init__(self):
        super().__init__()
        print('I am constructor for class P')


class A(P,Y):
    def __init__(self):
        super().__init__()
        print('I am constructor for class A')

class B(Y,Z):
    def __init__(self):
        super().__init__()
        print('I am constructor for class B')

class C(P,Z):
    def __init__(self):
        super().__init__()
        print('I am constructor for class C')

class D(P,Y,Z):
    def __init__(self):
        super().__init__()
        print('I am constructor for class D')

class MyClass:
    d = D()

