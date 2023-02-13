# loop using list
friends: list[str] = ["Cece", "Roko", "Niko"]

for friend in friends:
    print(friend)

# use pop() to remove idx el
friends.pop(0)

# append() new el
friends.append("Ziko")

# check for idx
print(friends[2])

# remove by el
friends.remove("Cece")

# if in syntax
if "Roko" in friends:
    print("it's a friend")
