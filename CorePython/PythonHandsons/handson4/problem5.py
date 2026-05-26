word=input("Enter the Word:")
lower=""
upper=""
for i in range(len(word)):
    if word[i].islower():
        lower+=word[i]
    elif word[i].isupper():
        upper+=word[i]
combined=lower+upper
print(combined)