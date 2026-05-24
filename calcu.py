
while True:
    print("please select an operation:")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    
    operation = input("operation?")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = float(num1)
    num2 = float(num2)


    if operation == "1":
        result = num1 + num2
        print("The result is: ", result)
    elif operation == "2":
        result = num1 - num2
        print("The result is: ", result)
    elif operation == "3":
        result = num1 * num2
        print("The result is: ", result)
    elif operation == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("The result is: ", result)

    again = input("Do you want to perform another calculation? (yes/no)")

    if again.lower() == "no":
        break
