def circle(radius):
    print("Area of Circle:",3.14*radius*radius)
    
def rectangle(length,breadth):
    print("Area of Rectangle:",length*breadth)
    
def square(side):
    print("Area of Square:",side*side)
    
while True:
    print("Menu Driven Program")
    print("1.Circle")
    print("2.Rectangle")
    print("3.Square")
    print("4.Exit")
    
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        r=int(input("Enter Radius:"))
        circle(r)
    elif choice ==2:
        l=int(input("Enter length:"))
        b=int(input("Enter breadth:"))
        rectangle(l,b)
    elif choice==3:
        side=int(input("Enter Side:"))
        square(side)
    else:
        print("Thank You!")
        break
    