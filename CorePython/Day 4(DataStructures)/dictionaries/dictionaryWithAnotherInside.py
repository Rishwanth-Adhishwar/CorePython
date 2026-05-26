myFamily = {
    'child1': {'name':'Ram', 'year':2005},
    'child2': {'name':'Raj', 'year':2004}
}

myfam = {
    'name':'Rishwa',
    'age':35,
    'mail':'arul@gmail.com'
}

print(myfam['age'])
print(myfam['mail'])

myfam['color']='purple'
print(myfam)

for x in myfam:
    print(x,myfam[x])
    
print(myfam.keys())
print(myfam.values())

print(myfam.items())
'''print(myfam.clear())
print(myfam)'''

print(myfam.pop('age'))
print(myfam.popitem())
print(myfam)


d={1:'one',2:'two'}
print(d.get(1,"Not Found"))
print(d.get(2,"Not Found"))

d1={2:'twooo'}
d.update(d1)
print(d)
