# another way of if statement, COMPARING NUMBERS
# passing 3 numbers,or 3 pieces of info

# def max_num(num1, num2, num3):
#     # specify condition
#     if num1 >= num2 and num1 >= num3:
#         # want info returned back
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#        return num3
#
# # calling new function and printing out in 1 stmt
# print(max_num(3,40, 5))

# COMPARING STRINGS
def max_num(num1, num2, num3):
    # specify condition
    if "DOG" == "DOG" and num1 != num3:
        # !=  "NOT EQUAL TO"
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
       return num3

# calling new function and printing out in 1 stmt
print(max_num(3,40, 5))