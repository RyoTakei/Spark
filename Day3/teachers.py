class Teacher:
    def __init__(self, name, age, subject, room_number, good_teacher):
        self.name = name
        self.age = age
        self.subject = subject
        self.room_number = room_number
        self.good_teacher = good_teacher

    def print_name(self):
        print("His/Her name is ", self.name)

    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False

    def teach_subject(self):
        print("This teacher teaches", self.subject)

    def room(self):
        print("This teacher teaches at room", self.room_number)

    def teacher_type(self):
        if self.good_teacher:
            print("This is a good teacher")
        else:
            print("This is a bad teacher")

my_teacher1 = Teacher("Ryo", 12, "Python", "0", True)
my_teacher2 = Teacher("Micah", 3, "Game", "0", False)
my_teacher3 = Teacher("Annika", 3, "Life", "A2", True)
my_teacher4 = Teacher("Novitt", 60, "Bio", "7", False)

my_teacher1.print_name()
my_teacher2.print_name()
my_teacher3.print_name()
my_teacher4.print_name()

print()

if my_teacher1.can_drive():
    print("teacher 1 can drive")
else:
    print("teacher 1 cannot drive")

print()

my_teacher1.teach_subject()
my_teacher2.teach_subject()
my_teacher3.teach_subject()
my_teacher4.teach_subject()

print()

my_teacher1.room()
my_teacher2.room()
my_teacher3.room()
my_teacher4.room()

print()

my_teacher1.teacher_type()
my_teacher2.teacher_type()
my_teacher3.teacher_type()
my_teacher4.teacher_type()