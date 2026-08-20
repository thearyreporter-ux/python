#inheritance
#single inheritance
class A:
    print("this is class A")
class B(A):
    pass
class C:
    def show_name(self):
        print("this is class C")
class D(C):
    def display(self):
        print("This is display from class D")
c = C()
#c.display()

class Teacher:
    def __init__(self, name, classroom):
        self.__name = name
        self.__classroom = classroom
        print("teacher has created")
class student(Teacher):
    pass
kanika = student("nika", 12)
