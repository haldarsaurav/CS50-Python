# https://cs50.harvard.edu/python/2022/psets/1/interpreter/ ************* Click for the Question! 

expression = input("Expression: ")  # get the user input
x, y, z = expression.split(" ")    # converting into the variables
new_x = float(x)    # changing the types of the variables
new_z = float(z)
if y == "+": # calculating the result and printing it
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z
print("The result is = ", round(result, 2))  #rounding off to 2 digits