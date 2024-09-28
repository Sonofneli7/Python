# if statements: help make decisions: execute code when certain conditions are true

is_male = False
# add another boolean var to mix
is_tall = True
# # if block with condition
# if is_male:
#     print("You are a male")
# else:
#     print("You are a female")

# using "or" in if stmt
# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#         print("You are neither a male nor tall")

# using "and" in if stmt
# if is_male and is_tall:
#     print("You are a tall male")
# else:
#         print("You are either not male or not tall")

# Checking to see more conditions
if is_male and is_tall:
   print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are either not male and not tall")