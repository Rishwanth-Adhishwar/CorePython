str=input("Enter a String:")
l=list(str)
lowCase,uppCase,nonChar=0,0,0
for i in l:
    if i.isalpha():
        if i.islower():
            lowCase+=1
        else:
            uppCase+=1
    else:
        nonChar+=1
print("Lower Case Letter:",lowCase) 
print("Upper Casee Letter:",uppCase)
print("Non Letter:",nonChar) 
            