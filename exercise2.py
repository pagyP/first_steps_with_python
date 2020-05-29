#print(type("Hello There!"))
#print(type(7))

#print(type(True))
#print(type(False))

#print(type("True"))
#print(type("False"))

#The book function converts the strings True and False to True
# print(bool("True"))
# print(bool("False"))

# #When the bool function is given an empty string it returns False
# print(bool(''))

# #Any other non empty string returns True
# print(bool(' '))
# print(bool("Hello There!"))

#The bool function converts any non-zero value to True but converts the value 0 to False
# print(bool(7))
# print(bool(1))
# print(bool(0))
# print(bool(-1))

# print(1 + 1 == 3)
# print(1+1==2)

#Operators perform an operation on operands which could be literal values, variables values
# or any identifier like a method or calss.  Operators can be split into these categories:
#Arithmetic operators
#Assignment operators
#Bitwise operators
#Comparison operators
#Identity operators
#Logical operators
#Membership operators

# Comparison operators
# The equality operator == is one of a family of operators that you can use to compare two values. The following table doesn't show all possible operators. These are the comparison operators you're likely to use most often.

# TABLE 1
# Operator	Description
# ==	Equality operator
# !=	Inequality operator
# >	Greater than operator
# <	Less than operator
# >=	Greater than or equal to operator
# <=	Less than or equal to operator

# print(3 == 4)
# print(3 != 4)
# print(3>4)
# print(3<4)
# print(3>=4)
# print(3<=4)

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number >1 and first_number <10:
    print("The value is between 1 and 10")

if first_number > 1 or second_number <1:
    print("At least one value is greater then 1")

print(not true_value)
print(not false_value)

if not first_number > 1  and second_number <10:
    print("both values pass the test")
else:
    print("both values do NOT pass the test")