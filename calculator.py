def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # if y != 0:    # need to comment out for testing divide by zero to get ZeroDivisionError
        return x / y
    # else:         # need to comment out for testing divide by zero to get ZeroDivisionError
    #     return "Error: Division by zero is not allowed by Benny."     # need to comment out for testing divide by zero to get ZeroDivisionError

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1-4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(num1)
    print(num2)

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    else:
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input. Please enter a valid choice.")
