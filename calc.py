print("This calculator will add two numbers together.")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    print("Invalid operation.")
print(f"The result is {result}.")
input("Press Enter to continue...")