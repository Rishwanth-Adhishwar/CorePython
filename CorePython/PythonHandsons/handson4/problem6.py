tup1=input().split(',')
tup2=input().split(',')

tup3=()

for i in range(len(tup1)):
    tup3+=(tup1[i]+tup2[i],)
    
print(tup3)