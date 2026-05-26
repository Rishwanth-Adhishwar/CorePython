la=[]
n=int(input("Enter the length of list:"))

for i in range(0,n):
    print("ENter the elemnent No {}:".format(i+1))
    element=int(input())
    la.append(element)
print(la)


lb=[]
n=int(input("Enter the length of list:"))
lb=input("Enter the input By Comma(,) Seperated:").split(',')
print(lb)

lc=list(map(int,input("Enter the input By Comma(,) Seperated:").split(',')))
print(lc)
