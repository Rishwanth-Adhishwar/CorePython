def increment(l2):
    for i in range(0,len(l2)):
        l2[i]+=5
    print("After:",id(l2))
    print(l2)
    
def increment2(l2):
   print("BeforeIncrement:",id(l2))
   l2=[1,2,3,4,5]
   for j in range(0,len(l2)):
       l2[j]+=5
   print("AfterIncrement:",id(l2))
   print(l2)
    
l1=[1,2,3,4,5]
print("Before:",id(l1))
print(l1)
increment(l1)
increment2(l1)