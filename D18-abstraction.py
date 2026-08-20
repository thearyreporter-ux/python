from abc import ABC, abstractmethod

class school(ABC):

    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def show_name(self):
        pass

    def show_year(self):
        print("school is operating for 5 years ")

class student(school):
    def show_name(self):
        print(f"student name: {self.name}")

class teacher(school):
    def __init__(self, name, subject):
        super().__init__(name, subject)
        self.__subject = subject
    def show_name(self):
        print(f"teacher name : {self.name}")

student1 = student("mony", 12)
student1.show_name()

teacher1 = teacher("kimsan", "math" )
teacher1.show_name()
