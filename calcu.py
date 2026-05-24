num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2 = float(num2)



print("Select operation:")
operation = input("operation?")   
operation = str(operation)

if operation == "+":
    result = num1 + num2
    print("The result is: ", result)
elif operation == "-":
    result = num1 - num2
    print("The result is: ", result)
elif operation == "*":
    result = num1 * num2
    print("The result is: ", result)
elif operation == "/":
    result = num1 / num2
    print("The result is: ", result)