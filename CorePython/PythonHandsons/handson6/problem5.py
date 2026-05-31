d={}

n=int(input("Enter No.of Key-Value pairs:"))

for x in range(n):
    key=input("Enter Key:")
    
    if key.isdigit():
        key=int(key)
    value=input("Enter Value:")
    
    d[key]=value
getV=input("Enter the key to access:")
if getV.isdigit():
    getV=int(getV)
print(d.get(getV))