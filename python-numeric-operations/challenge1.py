temp_in_fahrenheit = input("Temp in fahrenheit: ")
if temp_in_fahrenheit.isnumeric() ==  False:
    print("Input is not a number")
    exit()
temp_in_fahrenheit = int(temp_in_fahrenheit)
celsius = (temp_in_fahrenheit - 32) * 5/9
celsius = int(celsius)
print("Temp in celsius is: " + str(celsius))