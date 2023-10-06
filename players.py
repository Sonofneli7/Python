# slicing a list, specify index of first & last elements to work with

players = ['charles','martina','michael','florence','eli']
print(players[0:3])

# generating a subset of list
players = ['charles','martina','michael','florence','eli']
print(players[1:4])

# no starting index will begin at start of list
players = ['charles','martina','michael','florence','eli']
print(players[:4])

#including end of index, example want 3rd item to end
players = ['charles','martina','michael','florence','eli']
print(players[2:])

# Outputting last three players on roster
players = ['charles','martina','michael','florence','eli']
print(players[-3:])

# Looping through a slice
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())