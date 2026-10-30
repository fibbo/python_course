"""A for loop runs a block of code once for every item in a sequence.

This example loops over a range of numbers and prints only the odd ones.
"""

numbers = list(range(1, 1000, 3))


for n in numbers:
    if n % 2 == 1:
        print(n)
