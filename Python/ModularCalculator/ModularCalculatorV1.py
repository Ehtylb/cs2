# Modular Calculator - Version 1

def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    return num1 / num2


# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

# Call the correct function
if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    if num2 == 0:
        result = "Cannot divide by zero."
    else:
        result = divide_numbers(num1, num2)
else:
    result = "Invalid choice."

print("\nResult:", result)