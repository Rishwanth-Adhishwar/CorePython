str=input("Enter a String:")
l=str.split()
a=l[0]
b=l[1]
c=l[2]


print("{} {} {}".format(a,b,c))
print("{1} {0} {2}".format(a,b,c))
print("{third} {second} {first}".format(first=a,second=b,third=c))