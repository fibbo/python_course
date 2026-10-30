"""Divider exercise.

Build a divider line by repeating a character and print it. The character and the
number of repetitions are read from the user.
"""


# Returns the divider. This allows it to be used e.g., for writing to a file instead of printing it.
def divider(char, length):
    return char * length


# Prints the divider to the console. Uses the divider function to get the string to print.
def print_divider(char, length):
    print(divider(char, length))


# Reads the character and the number of repetitions from the user and returns the divider string.
def divider_from_input():
    char = input("Enter the divider character: ")
    length = int(input("Enter the repetitions: "))
    return divider(char, length)


print(divider_from_input())
