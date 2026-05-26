s1=input()
s2=input()

x=s1[0]+s2[0]
y=s1[(int)(len(s1)/2)]+s2[(int)(len(s2)/2)]
z=s1[len(s1)-1]+s2[len(s2)-1]

print(x+y+z)
