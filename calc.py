while True:
    number1 = input("Enter expression (or q to quit), enter the first number: ")
    if number1.lower() == "q":
        break
    number1 = float(number1)
    number2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /):")
    if operation == "+":
        result = number1 + number2
        print(f"The result is {result}.")
    elif operation == "-":
        result = number1 - number2
        print(f"The result is {result}.")
    elif operation == "*":
        result = number1 * number2
        print(f"The result is {result}.")
    elif operation == "/":
        if number2 == 0:
            print("Error: Division by zero.")
            continue
        result = number1 / number2
        print(f"The result is {result}.")
    else:
        print("Invalid operation.")
