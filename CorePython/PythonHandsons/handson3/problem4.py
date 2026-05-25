def soe():
    se=0
    for i in range(1,1001):
        if i%2==0:
            se=se+i
            
    return se

def soo():
    so=0
    for i in range(1,1001):
        if i%2!=0:
            so=so+i
            
    return so

evenSum=soe()
oddSum=soo() 
diff=evenSum-oddSum
print("Even Sum from 1 to 1000 is:",evenSum)           
print("Odd Sum from 1 to 1000 is:",oddSum)     
print("Difference Between them is:",diff)   