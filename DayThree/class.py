# Instance Variables
class Student:
    '''
    a class for each student
    '''
    pass

student1 = Student()

student1.first_name = "Ryo"
student1.last_name = "Takei"
student1.age = 15

student2 = Student()

student2.first_name = "Annika"
student2.last_name = "Lee"
student2.age = 6

print(student1.first_name)
print(student2.first_name)

################################

class Person:
    '''
    a class for each student
    '''

    def __init__(self, first, last, age):
        '''this function sets first_name, last_name, and age for each person'''
        self.first_name = first
        self.last_name = last
        self.age = age

person1 = Person("Ryo", "Takei", 15)
person2 = Person("Annika", "Lee", 6)

print(person1.first_name)
print(person1.age)
print(person2.last_name)




