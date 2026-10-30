"""Implement a simple calculator that can add two numbers.

The initial program misses the type conversion to int which leads in the addition
to string concatenation instead of numeric addition.
"""

print("Add two numbers")
a = int(input("Please enter the first number "))
b = int(input("Please enter the second number "))
print("The result of " + str(a) + " + " + str(b) + " is: " + str(a + b))


""" Below an example of how the f-string can improve the readability of the code and avoid the need for type conversion.
"""
a = 20
b = 10
res = a + b
print(f"The sum of {a} and {b} is {res}")
# Used to look like this:
# print("The sum of " + str(a) + " and " + str(b) + " is " + str(res))
