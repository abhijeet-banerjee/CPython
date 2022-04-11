def var_args(farg, *fargs):
    print('Formal Argument is %d' %farg)
    s=0
    for i in fargs:
        s+=i
    print('Sum is %d\n' %s)   


var_args(5,10,20)
var_args(5,10,20,40)
var_args(5,10,20,125,478,999,665)