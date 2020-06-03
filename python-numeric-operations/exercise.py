# #use the type() function to print the data type
# print(type('7'))
# print(type(7))
# print(type(7.1))

#the type function examines the value you pass it an an input parameter (the word between the parentheses) and
#returns the data type

#The isinstance() function allows you to assert that you expect a value to be a certain data type
# isinstance() tells you whether the value is what you expected.  True if your expectation is correct and 
#False if it's incorrect

# print(isinstance('7', str))
# print(isinstance(7, int))
# print(isinstance(7.1, float))

# print(isinstance(7,str))
# print(isinstance('7', int))
# print(isinstance('7.1', float))

#For now think of isinstance() as an easy way to compare the value and the data type you expect it to be

#The data type is part of the value, it is not a part of the variable that you might use
#to acess that value.  A variable can point to any value, regardless of the value's data type

# x = 'a string'
# print(type(x))
# x = 7
# print(type(x))
# x = False
# print(type(x))


