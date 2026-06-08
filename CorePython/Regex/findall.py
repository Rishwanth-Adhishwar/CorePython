import re
text="Hello RIshwanth, aWelcomeb to the python Concept of the Regular Expression,once again Welcome"

res=re.findall('Welcome',text)
print(type(res))

print(f"Result: {res}")
