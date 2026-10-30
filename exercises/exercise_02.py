"""Ascending order exercise.

Read three numbers and check if they are in ascending order, once with "and"
and once with a chained comparison.
"""

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x <= y <= z:
    print(True)

# Or even more elegant with a chained comparison:
if x <= y <= z:
    print(True)

# And if the result is the boolean value, you can just print the result of the comparison:
print(x <= y <= z)
