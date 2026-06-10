print ("Which operation do you want to perform?")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Modulus") 
print("5. Subtraction")
operation = input("Enter the number corresponding to the operation you want to perform: ")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def add_numbers(x, y):
    return x + y
def multiply_numbers(x, y):
    return x * y       
def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."
def modulus_numbers(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero is not allowed."
def subtract_numbers(x, y):
    return x - y
if operation == "1":
    result = add_numbers(x, y)
elif operation == "2":
    result = multiply_numbers(x, y)
elif operation == "3":
    result = divide_numbers(x, y)
elif operation == "4":
    result = modulus_numbers(x, y)
elif operation == "5":
    result = subtract_numbers(x, y)
else:
    result = "Invalid operation selected."
print("The result of the selected operation is:", result)