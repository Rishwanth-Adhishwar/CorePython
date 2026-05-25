birth_Date=input("Enter Your D.O.B:")

#year,month,day=birth_Date.split('-')
year=int(birth_Date.split('-')[0])
month=int(birth_Date.split('-')[1])
day=int(birth_Date.split('-')[2])
curr_year=2026

age=curr_year-year
print("Your Age is:",age,"years")
