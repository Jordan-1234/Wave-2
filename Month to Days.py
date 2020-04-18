# User input for the month
month_name = input("Name of the month: ")
# Group months with same amount of days
if month_name == "February":
    print("Number of days: 28/29 days")
elif month_name in ("April" , "June" , "September" , "November"):
    print("Number of days: 30")
elif month_name in ("January" , "March" , "May" , "July", "August" , "October", "December"):
    print("Number of days: 31 days")
# Else statement if month is spelt incorrect or not possible
else: 
    print("Incorrect Month Name ")