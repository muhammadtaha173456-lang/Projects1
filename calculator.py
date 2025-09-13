# calculator.py

# Get inputs
operation = input("Enter the operation: ")
num1 = float(input("Enter the first operand: "))
num2 = float(input("Enter the second operand: "))

# Perform calculation
if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    result = num1 / num2

# Display result
# If result is an integer value, show 1 decimal place; otherwise show 2
if result.is_integer():
    print(f"Result is {result:.1f}")
else:
    print(f"Result is {result:.2f}")
