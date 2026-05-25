#number DataType
num_1=10
print(type(num_1))

num_2=1.1045
print(type(num_2))

num_3=-244
print(type(num_3))


start=True
print(type(start))

cp=3+4j
print(type(cp))

#SequenceDataType(Strings,List,Tuples)
name="Rishwa"
print(type(name))

l1=[1,2,3,4,5,"rishwa",12.03]
print(type(l1))
print(type(l1[5]))

t1=(10,20,"Apple",4.50)#once created cannot be changed
print(t1)
print(type(t1))
print(type(t1[3]))

#Sets(unordered || Cannot have Duplicated ||once created cannot be changed)

s1={10,20,"Rishwa",55.09}
print(s1)
print(type(s1))

#None(used ti signify the absence of value,i neither same as false or 0)
myVar=None
print(type(myVar))
myVar=20
print(myVar)
print(type(myVar))

#Dictionaries(Should be represented as key(String is prefered): values)
student={"name":"Rishwa","age":"21","BloodGroup":"B+ve"}
print(student)
print(type(student))
print("AGE:",student["age"])

#Boolean:literals
x=(1==True)
print("X:",x)
y=(1==False)
print("Y:",y)
a=(True+4)
print("A:",a)
b=(False+10)
print("B:",b)

#Membership Opertaor:
a=[1,2,3]
print(2 in a)
print('1' in a)

print(10 not in a)
print(1 not in a)

n1=10
n2=30
sum1=n1+n2
print(sum1)
print(type(sum1))


sum2=float(n1+n2)
print(sum2)
print(type(sum2))

#input and output

fname=input("Enter your name:")
age=int(input("Enter your age:"))
print(fname)
print(age)
print(type(age))
print("The name is: ",fname,"\nThe age is: ",age)
print(f"My name is: {fname} \nAnd my age is: {age}")
print("apple","orange","Banana","Grapes",sep=",",end=".\n")
