import re
text="Hello RIshwanth, Welcome to the python Concept of Regular Expression"

res=re.search("^Hello.*Expression$",text)
print(type(res))
if(res):
    
    print("We Have a Match")
else:
    print("We don't have a Match")
    
