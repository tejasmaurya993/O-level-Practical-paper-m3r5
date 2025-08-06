#program to find your grade , above 90 grade A+ , above 80 grade A, above 70 grade B, above 60 grade c , otherwise fail.
grade = int(input("enter your marks :"))
if grade > 90 and grade <= 100:
    print("your grade is A+")
elif grade > 80 and grade <= 90:
    print("your grade is A")
elif grade > 70 and grade <= 80:
    print("your grade is B")
elif grade > 60 and grade <= 70:
    print("your grade is C")
elif grade >= 0 and grade <= 60:
    print("you are fail.")
else :
    print("enter the vaild marks")