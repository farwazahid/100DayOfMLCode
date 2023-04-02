#class MyClass:                                                 
#    x = 5                                                      
#                                                               
#    @classmethod                                               
#    def my_class_method(cls):                                  
#        print("This is a class method")                        
#        print("The value of x is:", cls.x)                     
#                                                               
#MyClass.my_class_method()                                      
#                                                               
#class MyClass:                                                 
#    @staticmethod                                              
#    def my_static_method():                                    
#        print("This is a static method.")                      
##MyClass.my_static_method()                                    
                                                                
                                                                
#Example                                                        
class Student:                                                  
#Attribute                                                      
    num_of_stud = 0                                             
    raise_marks = 1.04                                          
#Methods                                                        
    def __init__(self, first, last, marks):                     
        self.first = first                                      
        self.last = last                                        
        self.marks = marks                                      
        self.email = first + '.' + last + '@gmail.com'          
                                                                
        Student.num_of_stud +=1                                 
                                                                
    def fullname(self):                                         
        return '{} {}'.format(self.first, self.last)            
                                                                
    def apply_raise(self):                                      
        self.pay = int(self.marks * self.raise_marks)           
                                                                
    @classmethod                                                
    def set_raise_marks(cls, marks):                            
        cls.raise_marks = marks                                 
                                                                
    @classmethod                                                
    def from_string(cls, stud_str):                             
          first, last, marks = stud_str.split('-')              
          return cls(first, last, marks)                        
                                                                
                                                                
                                                                
    @staticmethod                                               
    def is_classday(day):                                       
        if day.weekday() == 5 or day.weekday() == 6:            
            return False                                        
        return True                                             
                                                                
                                                                
stud_1 = Student('Farwa', 'Zahid', 850)                         
stud_2 = Student('Aliha', 'Javed', 900)                         
                                                                
Student.set_raise_marks(1.04)                                   
                                                                
print(Student.raise_marks)                                      
print(stud_1.raise_marks)                                       
print(stud_2.raise_marks)                                       
                                                                
stud_str_1 = 'Aliza-Javed-768'                                  
stud_str_2 = 'Hina-Khan-869'                                    
stud_str_3 = 'Aiman-Butt-973'                                   
                                                                
first, last, marks = stud_str_1.split('-')                      
                                                                
                                                                
new_stud_1 = Student.from_string(stud_str_1)                    
                                                                
print(new_stud_1.email)                                         
print(new_stud_1.marks)                                         
                                                                
                                                                
import datetime                                                 
my_date = datetime.date(2016, 7, 10)                            
                                                                
print(Student.is_classday(my_date))                             
                                                                
                                                                