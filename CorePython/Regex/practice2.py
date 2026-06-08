import re
pattern=r'\b\w+ing\b'

text="Walking and talking are important acticities"
match=re.findall(pattern,text)
if match:
    print("Match Found: ",match.group())
else:
    print("No Match Found")