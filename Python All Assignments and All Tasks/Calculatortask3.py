# num1 = int(input("Enter your first number:")) 
# num2 = int(input("Enter your second Number:")) 

# addition = num1 + num2 
# subraction = num1 - num2 
# Multiplication = num1*num2 
# Division = num1/num2 

# print("The Addition of two number are:", addition) 
# print("The Subratction of two number are:", subraction) 
# print("The Multiplication of two number are:", Multiplication) 
# print("The Division of the two numbers are:",Division) 
# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}


def calculator():
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice in operations:
        result = operations[choice](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter a valid option.")


calculator()
