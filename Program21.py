#Program to find the largest number between 3 numbers by using if-elif-else statement.
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

if num1 > num2 & num1 > num3 :
    print("first number is largest")
elif num2 > num3 :
    print("second number is largest")
else:
    print("third number is largest")