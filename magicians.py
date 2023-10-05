# for looping through a list
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)


# other examples
cats = ['hairless','calico','tabby']
for cat in cats:
    print(cat)

dogs = ['boxer','pitbull','dane']
for dog in dogs:
    print(dog)

items = ['clothes','shower','clean']
for item in items:
    print(item)

# doing more  within for loop
magicians = ['alice','david','carolina']
for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")

# writing mult. lines of code in for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
      print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing code after a for loop, do not indent
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
      print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")