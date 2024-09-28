# List: store a bunch of data values: give a descriptive name
# can put string, numbers, booleans in array list
friends = ["Mike", "Maura", "Jon", "Paisley", "Danie"]
# fwd index   0        1        2
# bkwd index -3       -3       -1

print(friends)

# print out specific element by index
print(friends[2])

# print out specific element by back of index
print(friends[-2])

# making a copy of a list
friends2 = friends.copy()
print(friends2)

# selecting a range of elements
print(friends[1:4])
# selecting starting index/element and everything after
print(friends[3:])

# modifying an element
friends[1] = "Letty"
print(friends)

friends.sort()
print(friends)

#Luck numbers example: List functions and how to use
lucky_numbers =  [4, 8, 15, 16, 23, 42]

# extend function, append one list onto another
friends.extend(lucky_numbers)
print(friends)

# adding indiv. items to a list
friends.append("Creed")
print(friends)

# inserting an element at position: moves all other elements to the right
friends.insert(1, "Mia")
print(friends)

# removing an element at position: moves elements back left
friends.remove("Jon")
print(friends)

# pops item off end of list
friends.pop()
print(friends)

# find if something is on the list
print(friends.index("Paisley"))


# clear all the elements
friends.clear()
print(friends)

#sorting numbers in order
lucky_numbers.sort()
print(lucky_numbers)

# print them out in reverse order
lucky_numbers.reverse()
print(lucky_numbers)

