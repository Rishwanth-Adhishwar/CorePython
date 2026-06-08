import re
e_Pattern=r'.*  \S\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
text="Contact us at trainer@smartcliff.in or gayathri.manoj@smartcliff.in"
ef=re.findall(e_Pattern,text)
if ef:
    print("Email address found:",ef)
else:
    print("Email Address not Found")