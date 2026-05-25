def calculate_Hike(os,h):
    newSalary=(os+(os*h/100))
    
    return newSalary


oldSalary=float(input("Enter the Old Salary:"))
hike=float(input("Enter the Hike:"))

result=calculate_Hike(oldSalary,hike)
print("New Salary is:",result)