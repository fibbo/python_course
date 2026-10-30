"""Conditionals consist of if, elif and else statements.

An if statement adds potential branches to your code. If the condition is true,
the code block will be executed. If the condition is false, the code block will be skipped.

An elif statement is short for "else if" and allows you to check multiple conditions.
If the first condition is false, the program will check the next condition, and so on.

The else statement is optional and will be executed if all previous conditions are false.

Sometimes the order of the conditions matters. The first condition that evaluates to
true will be executed, and the rest will be skipped.
"""

number = int(input("Please enter a number: "))


if number > 34:
    print("The number is greater than 34.")
elif number > 23:
    pass
print(
    "This will always be executed because I removed the indentation in the source code."
)
