class Student:
    def __init__(self):
        self._name="python"
    def _funName(self):
        return "Method Here"
    
class Subject(Student):
    pass
o1=Student()
o2=Subject()

print(o1._name)
print(o1._funName())

print(o2._name)
print(o2._funName())
