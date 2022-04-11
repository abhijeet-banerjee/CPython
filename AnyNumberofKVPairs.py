def var_args(farg,**kwargs):
    print('Formal Argument %d\n' %farg)
    for x,y in kwargs.items():
        print("The value of {} is {}".format(x, y))
    print('--------------------------------------')


var_args(5,rno=10)
var_args(5,empno=1001,doj='20-April-2020',designation='Tester')
var_args(6,dr_prof_id=4578,specialization='ENT Surgeon',fees=450)
