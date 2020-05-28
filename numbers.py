print("First Number")
#if you don't use int function here sum will concatenate the two numbers as input takes them as string
#the input function is executed first and the the value is passed as an input parameter to the int function which
#converts from string to an integer
first_number = int(input())
print("Second Number")
second_number = int(input())
sum = first_number + second_number
print("sum: " +  str(sum)) #use the str function to convert the int to a string, otherwise the concatenation won't work