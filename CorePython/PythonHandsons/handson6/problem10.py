l= ["go","bat","me","eat","goal","run"]
charset= ['e','o','b', 'a','m','g', 'l'] 

for x in l:
    flag=True
    for ch in x:
        if ch not in charset:
            flag=False
    if flag:
        print(x)
    