print("Paisley is awesome")

# new line creation
print("Paisley \nis awesome")

# Escape character "\"
print("Paisley \"is awesome")

# print backslash
print("Paisley\is awesome")

# String variable creation and concatenation
phrase ="Paisley is awesome"
print(phrase + " and is cool!")

# using functions
phrase ="Paisley is awesome"
# all lowercase chars
print(phrase.lower())

# all uppercase chars
print(phrase.upper())

# checking if all uppercase chars
print(phrase.isupper())

# combining functions: 1st convert to all upper, 2nd checks if all upper
print(phrase.upper().isupper())

# find length
phrase ="Paisley is awesome"
print(len(phrase))

# get indiv. chars in string: specify index in []
phrase ="Paisley is awesome"
print(phrase[0])

# use index function to find specific char or string by passing a param/ giving a value
phrase ="Nelson is awesome"
print(phrase.index("w"))

# replace function: by giving 2 parameters, 1 = original 2= replacement
phrase ="Nelson is awesome"
print(phrase.replace("is", "was"))