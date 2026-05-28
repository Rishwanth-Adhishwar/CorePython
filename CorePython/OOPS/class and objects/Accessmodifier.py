class Student:
    def __init__(self):
        self.name="Shon"#public
        self.__age=20 #private
        self._gender='male'
obj=Student()
print(obj.name)
print(obj.__age)
print(obj._gender)