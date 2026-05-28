class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print("Details:",self.name,self.color,self.price)
    def max_speed(self):
        print("Max Speed of Vehicle is 150")
    def change_gear(self):
        print("Vehicle change 6 gear")
        
class Car(Vehicle):
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print("Details:",self.name,self.color,self.price)
    def max_speed(self):
        super().max_speed()
        print("Max speed of car is 750")
    def change_gear(self):
        super().change_gear()
        print("Car change 5 gear")
        
v=Vehicle("Yamaha","Black",200000)
v.show()
v.max_speed()
v.change_gear()

c=Car("Porsche","Ceramic Red",4000000)
c.show()
c.max_speed()
c.change_gear()
        
    
        