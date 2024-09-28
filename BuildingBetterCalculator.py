# User enter 1st number, enter operator, enter 2nd number. Then executes code

# get user input and quickly convert to number
num1 = float(input("Please enter your first number: "))

op = input("Please enter your choice of operator, eg( +, -, *, etc...): ")

num2 = float(input("Please enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("You entered an invalid operator!!!")