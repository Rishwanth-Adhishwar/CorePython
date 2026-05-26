t=tuple()
print(t)

t=tuple("aeiou")
print(t)

s=[1,2,3]
t=tuple(s)
print(t)

t1=(10,20,30,40,50)
print("Before:",id(t1))
t1=(100,)+t1[1:]
print(t1)
print("After:",id(t1))
