import traceback
try:
    num=int(input("Enter a positive Integer:"))
    if num<=0:
        raise ValueError("This is a negative Number!")
except ValueError as e:
    print(e)
    traceback.print_exc()
    
print("Sucess")