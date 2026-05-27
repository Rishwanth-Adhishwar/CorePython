file1=open("file1.txt","w")
ul=input("Enter:").split(',')
for i in ul:
    file1.write(i + "\n")

file1.close()

file2=open("file1.txt",'r')

allContent=file2.readlines()

print("".join(allContent))
