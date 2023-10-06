# working with tuples, storing collections of items that may change thru life of program
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# tuples defined by use of a comma
my_t =(3,)

# looping through all values in a Tuple, using a for loop
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# writing over a tuple, can't modify tuple but can assign a new value to a variable
dimensions = (200, 50)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# use tuples when want to store a set of value that shouldn't be changed in program.