# MOD3 Lecture activities
# 9/4/2025

# animals.py

# Ask the first question
legs = input("Does it have legs [y/n]: ")

if legs == "y":
    # If it has legs, ask if it's fluffy
    fluffy = input("Is it fluffy [y/n]: ")
    if fluffy == "y":
        print("It's a cat!")
    else:
        print("It's a gator!")
else:
    # If it does not have legs, ask if it lives on land
    land = input("Does it live on land [y/n]: ")
    if land == "y":
        print("It's a snake!")
    else:
        print("It's a shark!")
