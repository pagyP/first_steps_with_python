#The in keyword allows us to iterate through each item in a list, but 
# can laso be used to test whether an item belongs to a list
# numbers = [1,3,5]

# print(5 in numbers)
# print(8 in numbers)

# print(5 not in numbers)
# print(8 not in numbers)

#the for keyword allows us to iterate through each item in a list

# the for keyword
#the variable name that will hold the next item in the list
#the in keyword
#the variablee name of the list
#the colon : which ends the statement

# cities = ["Chicago", "London", "Tokyo"]

# for city in cities:
#     print(city)

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()

# for number in numbers:
#     if number > 42:
#         break
#     print(number)

# import random
# numbers=[]

# while len(numbers) <5:
#     numbers.append(random.randint(1, 100))

# for number in numbers:
#     print(number)
#     if number >= 90:
#         print('Found at least one number greater then 90')
#         break
# else:
#     print('No numbers greater than 90')

# print('complete')

# values = ["laptop", 7, "phone", 3, "dslr", 5]
# equipment = []

# for value in values:
#     if isinstance(value, str) == False:
#         continue
#     equipment.append(value)

# print(equipment)

# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# for suit in suits:
#     for rank in ranks:
#         print(f'{rank} of {suit}')

import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)


# Use the in and not in keywords as part of a Boolean expression to test whether a value is part of a list.
# Use the for statement to iterate through all items in a list. Also use the statement to execute a code block that puts the current item in scope to be inspected in the logic of the code block.
# Use the continue statement to skip the remaining code block logic and continue to the next list item that's assigned by the for statement.
# Use the break statement to break out of the for statement prematurely.
# Use the else statement to create a code block that executes after you use the for statement to iterate through all items in the list.
# Nest for statements to create a list of every combination of two lists.
# Use the random module's choice() and choices() functions to select one or many items from the list, respectively



