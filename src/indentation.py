"""Indentation decides which lines belong to a block of code.

Many languages use curly braces to group code. Python uses indentation instead:
all lines after a colon that are indented by the same amount form one block.
The block ends at the first line that is indented less again.

Use 4 spaces for each level of indentation and don't mix tabs and spaces.
"""

temperature = 25

# Both indented lines belong to the if block and only run if the condition is true.
if temperature > 20:
    print("It is warm.")
    print("Let's go swimming.")

# This line is not indented, so it runs no matter what the temperature is.
print("This always runs.")


# Blocks can be nested. Each level is indented by 4 more spaces.
for number in range(1, 6):
    print(f"Checking {number}")
    if number % 2 == 0:
        print(f"{number} is even")
    print("Done with this number")

print("Done with the loop")


# Moving a line in or out of a block changes what the program does.
# The first print runs in every iteration, the second one only once at the end.
total = 0
for number in [1, 2, 3]:
    total = total + number
    print(f"Inside the loop: {total}")
print(f"After the loop: {total}")


# The body of a function is an indented block as well.
def greet(name):
    greeting = f"Hello {name}"
    return greeting


print(greet("Monty Python"))


# A block must not be empty. Use pass if you don't want to do anything yet.
if temperature < 0:
    pass


# Wrong indentation stops the program before it even starts, so this example is
# commented out. Remove the # from both lines to see the IndentationError.
# if temperature > 20:
# print("It is warm.")
