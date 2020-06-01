#Helper functions are provided by Python to format strings or modify its contents

# #The capitalize function ensures that the first characterf in a string is capitalized
# #below we are calling the capitalize function as a member of the str class
# #we access the str helper methond but using the member access operator, a period symbol .
# message = str.capitalize("first message")
# print(message)

# #here well call the function as a member of the literal string
# message = "second message".capitalize()
# print(message)

# #here we call the function as a member of a variable
# message = "third message"
# print(message.capitalize())

# message = "hello world"
# print(message.lower())
# print(message.upper())

# message = message.title()
# print(message)
# print(message.swapcase())

#the count function provides the number of times a specified character is used in a string
# location = "Mississippi"
# print(location.count("s"))

# #When you want to know how many letters are in a string use the len() method
# print(len("how many letters in this string?"))

#you can use the startswith and endswiths functions to inspect the contents of a 
#string to se if it matches what you expected it to start or end with
# message = "racecar"
# print(message.startswith("r"))
# print(message.startswith("a"))
# print(message.startswith("ra"))

# print(message.endswith("r"))
# print(message.endswith("a"))
# print(message.endswith("ar"))

#the find method locates the zero based position of one string inside another string
# message = "The quick brown fox jumps over the lazy dog"
# print(message.find("q"))

# print(message.find("t"))
# print(message.find("T"))

# message = "    middle     "
# print("." + message.lstrip() + ".")
# print('.' + message.rstrip() + '.')
# print("." + message.strip() + ".")

#the replace() function swaps every instance of a string with a different string

# message = "brevity is the essence of wit"
# message = message.replace("essence", "soul")
# print(message)

#the rjust() and ljust() methods add empty space characters to a string to provide justification to the right or left
message = "howdy"
print(message.rjust(20))
print(message.rjust(20, "-"))
print(message.ljust(20))
print(message.ljust(20, "-"))


