def fact(num):
    if(num==1):
        return 1
    else:
        return(num*fact(num-1))

number=int(input("Enter the No:"))
factorial=fact(number)
print("Factorial:",factorial)