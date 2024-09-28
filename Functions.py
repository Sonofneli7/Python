# Functions: collections of code: code blocks: task performance
# call function when wanting to do task

# good practice naming functions, all lowercase, underscore when mult. words

def say_hi():
    print("Hello User")

#executes 1st print, calls function, then executes 2nd print
print("Top")
# calling the function
say_hi()
print("Bottom")

# passing a param to function: giving it information
def say_hi_user(name,age, age1):
    print("Hello " + name + ", Your age is " + age + " or " + str(age1))


say_hi_user("Nelson", "43", 43)
#hard coding the name into the parameter:
say_hi_user("Paisley", "1", 1)