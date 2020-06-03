print("Simple Calculator!")

first_number = input("Enter the first number: ")
if first_number.isnumeric() == False:
    print("Please input a number")
    exit()

operation = input("Operation? ")

second_number = input("Enter the second number: ")
if second_number.isnumeric() == False:
    print("Please input a number")
    exit()

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == "+":
    result = first_number + second_number
    label = "sum"
elif operation == "-":
    result = first_number - second_number
    label = "difference"
elif operation == "*":
    result = first_number * second_number
    label = "product"
elif operation == "/":
    result = first_number / second_number
    label = "quotient"
elif operation == "**":
    result = first_number ** second_number
    label = "exponent"
elif operation == "%":
    result = first_number % second_number
    label = "modulus"

else:
    print("Operation not recognised")
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))