# Using variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


# using f-strings to compose a msg
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# adding whitespace to string w/ tabs & newlines
print("Python")
print("\tPython")

# adding newline in a string
print("Languages: \nPython\nC\nJavaScript")

# String whitespace from string on right side
favorite_language = 'python  '
favorite_language.rstrip()
# result 'python'

# remove whitespace permanently: assoc. stripped value w/ variable name
favorite_language = 'python  '
favorite_language = favorite_language.rstrip()

# String whitespace from string on left side 
favorite_language = '  python'
favorite_language.lstrip()


# String whitespace from string on both sides
favorite_language = '  python  '  
favorite_language.strip()