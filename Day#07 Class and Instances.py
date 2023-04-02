class student:
    pass
stud_1 = student()
stud_2 = student()
print(stud_1)
print(stud_2)
stud_1.first = 'Farwa'
stud_1.last = 'Zahid'
stud_1.email = 'farwazahid427@gmail.com'
stud_1.pay = 32000


stud_2.first = 'Muqadas'
stud_2.last = 'Zahid'
stud_2.email = 'muqadaszahid@gmail.com'
stud_2.pay = 35000
print(stud_1.first)
print(stud_2.last)



class Student:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pat = pay
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #first name, last name are pay are arguments
    #this is the first method
stud_1 = Student('Farwa', 'Zahid', 32000)
stud_2 = Student('Muqadas', 'Zahid', 35000)

print(Student.fullname(stud_1))
print(stud_1.first)
print(stud_2.last)
print(stud_1.fullname)

