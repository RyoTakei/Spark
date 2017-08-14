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
    '''class for each student'''

    def __init__(self, first, last, age, student_id = 111111):
        '''this function sets first_name, last_name, and age for each person'''
        self.first_name = first
        self.last_name = last
        self.age = age
        self.student_ID = student_id

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def email(self):
        return "{}@bsd48.org".format(self.student_ID)

    def set_age(self, age):
        self.age = age

    def birthday(self):
        self.age += 1

    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False



person1 = Person("Ryo", "Takei", 15, 463108)
person2 = Person("Annika", "Lee", 6)

print(person1.first_name)
print(person1.age)
print(person2.last_name)
print(person2.full_name())
print(person1.full_name())
print(person1.email())
print(person2.email())

print(person2.age)
person2.birthday()
print(person2.age)


