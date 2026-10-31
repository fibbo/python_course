"""Running total exercise.

Keep asking for numbers and add them up until the user types "done".
"""

total = 0
while True:
    value = input("Please enter a number or type done to quit: ")
    if value.lower() == "done":
        break
    total += float(value)

print(f"The total sum is {total}")
