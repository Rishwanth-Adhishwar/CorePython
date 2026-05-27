try:
    a=int(input("Enter No1:"))
    b=int(input("Enter No2:"))
    c=a/b;
    print(c)
except(ZeroDivisionError):
    print("Can Divide By Zero!")
except(TypeError):
    print("Invalid Type! should be integer")
else:
    print("No Exception Occurs")
finally:
    print("I will execute always")

    