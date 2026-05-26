s1=input("Enter a String:")
l1=s1.split(" ")

for i in l1:
    l=False
    n=False
    
    for j in i:
        if j.isalpha():
            l=True
            
        if j.isnumeric():
            n=True

    if l and n:
        print(i)