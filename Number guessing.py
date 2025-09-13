# number guessing thingy

import random

number = random.randint(1, 50)
print("🤖 I picked a number between 1 and 50. Can you guess it?")

while True:
    guess = int(input("Your guess: "))
    if guess < number:
        print("Too low! 📉")
    elif guess > number:
        print("Too high! 📈")
    else:
        print("Correct! 🎉")
        break
