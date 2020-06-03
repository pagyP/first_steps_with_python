# first_value = 5
# second_value = 4

# sum = first_value + second_value
# difference = first_value - second_value
# product = first_value * second_value
# quotient = first_value / second_value
# modulus = first_value % second_value
# exponent = first_value ** second_value 

# print('Sum: ' + str(sum))
# print('Difference: ' + str(difference))
# print('Product: ' + str(product))
# print('Quotient: ' + str(quotient))
# print('Modulus: ' + str(modulus))
# print('Exponent: ' + str(exponent))

# Python follows the PEMDAS acronym, which indicates the order in which the operations should be performed.

# Parentheses: Resolve operations between parentheses first.
# Exponents: Resolve exponents.
# Multiplication: Perform multiplication, from left to right.
# Division: Perform division, from left to right.
# Addition: Perform addition, from left to right.
# Subtraction: Perform subtraction, from left to right.

# print(3 + 4 * 5)
# print((3 + 4) * 5)

#Division - when you perform a division you provide a dividend and a divisor.  if the values are
#of an int type they implicitly result in a quotient of type float
# first_value = 5
# second_value = 4

# quotient = first_value / second_value

# print(type(quotient))
# print(quotient)

# pi = 3.14
# print(type(pi))
# print(int(pi))
# #
# #the round() function avoids truncation, that avoids removing numbers after the .
# print(round(pi))

# uptime = 99.99
# print(type(uptime))
# print(int(uptime))
# print(round(uptime))
#The round() function provides a way to perform rounding and conversion from a float value into an int value.

# You can use round to round to a certain number of decimal points
first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)
#To call a function and pass more than one argument, you use a comma (,) to separate each argument.
#  As you'll learn when we dive deeper into functions, you can create functions that have optional input parameters. In this case,
#  if you don't supply the second argument, the round() function defaults to 0 places after the decimal, which gives you an int value.