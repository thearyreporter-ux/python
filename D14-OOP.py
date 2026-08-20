#class
class animal:
    color = "gray"
    year = 2
dog = animal()
dog.coloe = "black"
dog.year = 3
cat = animal()
cat.color = "white"
cat.year = 1



print(dog.color)
print(cat.color)
print(f"dog year is {dog.year}")
print(f"cat year is {cat.year}")


#method in class
class person:
    name = "kaka"
    gender = "female"
    school = "ngs"
    graducated = False

    def show_name(self):
        print(f"my name is {self.name}")
        print(f"my gender is {self.gender}")
        print(f"my graducated is {self.graducated}")

sok = person()
sok.show_name()