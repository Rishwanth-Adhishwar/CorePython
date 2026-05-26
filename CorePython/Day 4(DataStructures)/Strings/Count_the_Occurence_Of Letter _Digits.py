s = input("Enter a String: ")

letter = 0
digit = 0

for i in s:
    if i.isnumeric():
        digit += 1
    elif i.isalpha():
        letter += 1
    else:
        pass

print("Digit:", digit)
print("Letter:", letter)