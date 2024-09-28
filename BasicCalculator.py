# Building a basic calculator

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")

# by default will convert input into a string
# convert the strings into numbers: use a float to do whole numbers or decimals
result = float(num1) + float(num2)

print(result)