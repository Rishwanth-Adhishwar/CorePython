#Inserting element to list
t=list()
print(t)
print(type(t))
name="Rishwa"
t=list(name)
print(t)
print(type(t))

#Deletion of Entire and Single ELement in List
del t[1]
print(t)
del t
print(t)

#Traversing List
l1=['Red','Asscent','Black','Green']

for i in range(len(l1)):
    print(l1[i])