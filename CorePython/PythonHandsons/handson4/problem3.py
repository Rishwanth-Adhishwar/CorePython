string = input("Enter a String:")
newString=""
for i in string:
    if i.isalpha() or i.isnumeric():
        newString=newString+i
    else:
        newString=newString+'#'
print(newString)