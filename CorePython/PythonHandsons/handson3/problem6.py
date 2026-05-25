def increment_calc(salary,rating):
    if rating>=1 and rating<=4:
        increment=salary*(10/100)
        print(salary+increment)
    elif rating>=4 and rating<=7:
        increment=salary*(25/100)
        print(salary+increment)
    elif rating>=7 and rating<=10:
        increment=salary*(30/100)
        print(salary+increment)
    else:
        print("Invalid Input")

salary=float(input("Enter the Salary:"))
rating=float(input("Enter the rating:"))
increment_calc(salary,rating)

    