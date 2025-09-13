# letters.py

# Ask the user for a word
word = input("Enter a word: ")

# Ask the user for the letter to count
letter = input("Enter the letter to count: ")

# Count how many times the letter appears in the word
count = word.count(letter)

# Print the result
print(f"{letter} appears {count} times.")
