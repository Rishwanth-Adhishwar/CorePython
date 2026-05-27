f=open("myFile.txt",'w')

content=f.write("Hi,I am RIshwanth Adhishwar K")
print(content)
f.close()

f1=open("fileMy.txt",'w')
marks=58
c=f1.write(str(marks))
print(c)
f1.close()

f2=open("a.txt",'w')
names=['Arjun is good Boy in world\n','babu is bad boy in world\n','venkat is Funnier in World\n']
f2.writelines(names)
f2.close()