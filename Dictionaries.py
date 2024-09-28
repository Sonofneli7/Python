# Dictionaries: storing info in key value pairs
# key create a bunch of key value pairs in dictionary && can refer to it thru key
# Dictionary = have word && definition assoc. w/ word
# word = Key  definition = Value

# program to convert 3 digit month name into the full month name ie: Jan -> January

monthConversions = {
#   Key  : Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

# Access  key value pairs from w/in dictionary
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))

# with get function, can specify/ pass in a default value to use if key not found
print(monthConversions.get("Luv","Not a valid Key"))
#                           Key      Value

# Can use numbers in a dictionary
monthConversion1 = {
#   Key  : Value
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",

}

print(monthConversion1.get(0))