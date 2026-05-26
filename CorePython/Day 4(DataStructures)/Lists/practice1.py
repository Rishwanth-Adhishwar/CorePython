def appendAnElement(k1):
    n=int(input("Enter the Elment to Append:"))
    k1.append(l1)
    
def insertAnElement(k2):
    n=int(input("Enter the Elment to Insert:"))
    k2.insert(len(k2)-1,n)
def appendListToList(k3):
    l2=[6,7,8,9,10]
    k3.extend(l2)
def modifyExistingList(k3):
    k3[0]=int(input("Enter the Elment to modify:"))
    
def deleteExistingElementList(k3):
    del k3[int(input())]

def deleteExistingElementListValue(k3):
    k3.remove(2)
    
def sortA(k2):
    k2.sort()
def sortD(k3):
    k3.sort(reverse=True)
def displayList(k3):
    print(k3)
    

while True:
    l1=[1,2,3,4,5]
    print("1.Append an Element")
    print("2.Insert an Element")
    print("3.Append a list to given list")
    print("4.modify an existing list")
    print("5.Delete an existing element in list")
    print("6.Delete an existing element with a given value")
    print("7.Sort Ascending")
    print("8.Sort Descending")
    print("9.Display list")    
    print("10.Exit")
    choice=int(input("Enter the Choice:"))
    if choice ==1:
        appendAnElement(l1)
    elif choice ==2:
        insertAnElement(l1)
    elif choice ==3:
        appendListToList(l1)
    elif choice==4:
        modifyExistingList(l1)
    elif choice==5:
        deleteExistingElementList(l1)
    elif choice==6:
        deleteExistingElementListValue(l1)
    elif choice==7:
        sortA(l1)
    elif choice==8:
        sortD(l1)
    elif choice==9:
        displayList(l1)
    elif choice==10:
        break
    else:
        print("Invalid Choice")
        
    
    