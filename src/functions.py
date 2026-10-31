"""Functions group code under a name so it can be reused.

A function can take arguments and can return a value with the return statement.
If there is no return statement, the function returns None.
"""


def divider():
    print("++++++++++++++++")


def combine_score(base, points_scored):
    total_score = base + points_scored
    return total_score


numbers = [1, 2, 3, 55, 6, 7]

total = 0
for n in numbers:
    total = combine_score(total, n)
    divider()
    print(total)

print(total)

# divider() has no return statement, so it returns None.
# The output that you see in the console is from the print statement in the function,
# not from the return value.
result = divider()
print(result)
