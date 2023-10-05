motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# change value of the first item
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to end of list
motorcycles.append('ducati')
print(motorcycles)

# using appending to build lists dynamically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# inserting items to a list, add element at any position in list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove element using del statement, permanently removes
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# remove element using pop method,  removes last item and returns item to list

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop method to show last motorcycle owned
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# pop items from anywhere on list
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# use remove method w/ value being removed from list
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")




