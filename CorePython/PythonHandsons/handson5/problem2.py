a=input("Enter set a:").split(',')
b=input("Enter set b:").split(',')

setA=set(a)
setB=set(b)

print(setA.symmetric_difference(setB))