# medicine = "Coughussin"
# dosage = 5
# duration = 4.5

# #{} are replacement fields.  We use them here without any values inside them, we call the format() function and pass 
# #in the values we want to substitue in each replacement field in the order in which they appear
# instructions = "{} - Take {} ML by mouth every {} hours".format(medicine, dosage, duration)
# print(instructions)

# #here we fill the replacement fields with a zero based numeric value which accesses the argument passed 
# #into the format() function.  You can use the arguments in any position of your format string
# instructions = "{2} - Take {1} ML by mouth every {0} hours".format(medicine, dosage, duration)
# print(instructions)

# #here the replacement fields are filled with variable names.  Those variables names are passed as named arguments
# #in the format() function
# instructions = "{medicine} - Take {dosage} ML by mouth every {duration} hours".format(medicine = "Sneezergen", dosage = 10, duration = 6)
# print(instructions)

# name = "World"
# #here we create replacement fields and fill with the name of the variable we want to substitute in 
# message = f'Hello, {name}.'
# print(message)

# #here the variable count is set to an int and value is a float.  The format atring takes care of the 
# #data type conversion for us so we don't need to call str() around the values
# count = 10
# value = 3.14
# message = f'count to {count}. Multiply by {value}.'
# print(message)


# width = 5
# height = 10
# print(f'The permiter is {(2 * width) + (2 * height)} and the areas is {width * height}.')

#format specifiers
value = "hi"
print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
