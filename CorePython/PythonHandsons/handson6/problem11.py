l=[('for', 24), ('Gods', 8),('creates', 30)]

def secondIndex(x):
    return x[1]

l.sort(key=secondIndex)
print(l)