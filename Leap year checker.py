year=int(input("Enter year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("The year", year, "is a leap year.")
else:
    print("The year", year, "is not a leap year.")