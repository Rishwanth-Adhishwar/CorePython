class ConstructorDemo:
    def __init__(self,name):
        self.name=name
        
    def say_hi(self):
        print("Hello my name is:",self.name)
        
obj=ConstructorDemo("Rishwanth")

obj.say_hi()
