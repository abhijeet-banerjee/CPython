from AbhijeetBanerjee.Inheritance_Teacher import *

class Student(Teacher):

    def setMarks(self,mrk):
        self.mrk = mrk
    def getMarks(self):
        return self.mrk


s = Student()
s.setName("Ramesh")
s.setId(125)
s.setAddr('Ville Street, London')
s.setMarks(85.56)

t = Teacher()
t.setName('Anand Kumar')
t.setId(145)
t.setAddr("Lucknow UP")
print('Name {}, Id {}, Address {}, Marks {}'.format(s.getName(),s.getId(),s.getAddr(),s.getMarks()))
print('Name {}, Id {}, Address {}'.format(t.getName(),t.getId(),t.getAddr()))

