d={}
print(d)

d[0]=input("D[0]= ")
d[2]=input("D[2]= ")
d[3]=input("D[3]= ")
print(d)

d[2]=input("D[2]= ")
print(d)

v1=input("Nested key 1 value:")
v2=input("Nested key 2 value:")

d[5]={"Nested":{"1":v1,"2":v2}}
print(d)