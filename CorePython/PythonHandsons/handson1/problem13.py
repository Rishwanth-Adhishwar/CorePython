monthlyIncome = float(input("Enter Your Monthly Income: "))
expenses = input("Enter the expenses separated by space: ")
expensesList = expenses.split()
totalExpense = 0
for i in range(len(expensesList)):
    totalExpense = totalExpense + float(expensesList[i])
remaining = monthlyIncome - totalExpense
print("Total Expenses:", totalExpense)
print("Remaining Budget:", remaining)