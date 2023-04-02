class Student:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

stud_1 = Student('Farwa', 'Zahid', 32000)
stud_2 = Student('Muqadas', 'Zahid', 35000)


print(Student.raise_amount)
print(stud_1.raise_amount)
print(stud_1.raise_amount)


