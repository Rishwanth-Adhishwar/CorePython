mark=int(input("Enter the mark:"))

if mark>90:
    print("O")
elif mark>81 and mark<90:
    print("A")
    
elif mark>71 and mark<80:
    print("B")
    
elif mark>61 and mark<70:
    print("C")
    
elif mark>50 and mark<60:
    print("D")
    
else:
    print("F")
    