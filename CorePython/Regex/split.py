import re
text="Hello Rishwanth, aWelcomeb to the python Concept of the Regular Expression,once again Welcome"

res=re.split(' ',text)
print(type(res))

print(f"Result: {res}")
print(res[0])