mo=open("a.txt",'r')
word=mo.read(11)
print(word)
mo.close()

mo=open("a.txt",'r')
w1=mo.readline()
print(w1)
mo.close()

mo=open("a.txt",'r')
w2=mo.readlines()
w3="".join(w2)
print(w3)

