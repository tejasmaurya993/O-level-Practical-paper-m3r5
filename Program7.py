#Program to display months and days for entered no. of days

days = int (input("Enter number of days :"))
months = int(days/30)
day = days % 30
print("the total months :", months)
print("the total days :", day)
