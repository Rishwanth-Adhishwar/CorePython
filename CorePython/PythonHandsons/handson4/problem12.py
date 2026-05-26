str1=input("Enter 1st String:")
str2=input("Enter 2nd String:")

str2=str2[::-1]
result=""
for i in range(len(str1)):
    result+=str1[i]+str2[i]
    
print(result)