# Prompt the user for an arithmetic expression
expression = input("Please enter an arithmetic expression (in the format 'x y z'): ")

# Split the expression into three parts using the split() method and whitespace as the separator
x, y, z = expression.split()

# Convert x and z to integers using the int() function
x = int(x)
z = int(z)

# Calculate the result based on the operator in y using a conditional statement
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
else:
    result = x / z

# Output the result as a floating-point value formatted to one decimal place using the format() method
print("{:.1f}".format(result))
