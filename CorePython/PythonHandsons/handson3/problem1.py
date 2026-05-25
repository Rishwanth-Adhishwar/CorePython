def sum_Of_Odd_Even(num):
    e,o=0,0
    oddEvenList=num.split()
    for i in oddEvenList:
        i=int(i)
        if i%2==0:
            e=e+i
        else:
            o=o+i
        
    
    print("Even Sum:",e)
    print("Odd Sum:",o)
            
            

numbers=input("Enter the Numbers:")
sum_Of_Odd_Even(numbers)