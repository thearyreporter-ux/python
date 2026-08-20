#encapsulation
class person:
    def __init__(self, id, name, dob):
        #public
        self.id = id
        #private
        self.__name = name
        #protected
        self._dob = dob
p1 = person(101, "kaa", "1/1/2000")
print(p1.id)
print(p1.__name)
print(p1.dob)