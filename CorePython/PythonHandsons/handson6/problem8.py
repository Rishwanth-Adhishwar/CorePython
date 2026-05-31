l=[(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

key=int(input("Enter key Length:"))

for x in l:
    if len(x)==key:
        l.remove(x)
        
print(l)