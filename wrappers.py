# wrappers.py

# Ask the user how much money they have
money = int(input("How much money do you have: "))

# Each candy bar costs $4
cost = 4

# Initial number of candy bars
bars = money // cost

# Wrappers equal to bars initially
wrappers = bars

# Keep exchanging wrappers for new bars
while wrappers >= 3:
    new_bars = wrappers // 3
    bars += new_bars
    wrappers = (wrappers % 3) + new_bars  # leftover wrappers + new wrappers

# Print the result
print(f"You can purchase {bars} candy bars!")
