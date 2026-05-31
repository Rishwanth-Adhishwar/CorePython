import math
t=input("Enter numbers seperated by commas:").split(',')
tup=tuple(t)
m=0
for x in tup:
    x=int(x)
    if x>m:
        m=x
print(m)
        
