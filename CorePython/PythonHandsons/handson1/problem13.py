monthlyIncome=float(input("Enter Your Monthly Income:"))
expences=input("Enter the expenses by space seperated:")
list=expences.split(' ')
tExpences=list.__add__
print("Remaining Budget $",(float)(monthlyIncome-tExpences))

