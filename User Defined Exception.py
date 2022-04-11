'''
Calculating Tax in accordance with the salary (18% of it)
If salary is less than 10K, flag an exception as 'Non Taxable Amount'
'''
import logging
class Person(Exception):

    def __init__(self,sal):
        self.sal = sal

    def calculateTax(self):
        tax = 0.0
        if self.sal > 10000:
            tax = (1.18 * self.sal)
            print('Total Tax Payable = ',tax)
        else:
            raise Person("Non Taxable Amount")


p = Person(1000)
logging.basicConfig(filename='info.txt', level=logging.CRITICAL)
try:
    p.calculateTax()
except Person as e:
    print(e)
    logging.exception(e)
finally:
    print('Thanks for your time')



