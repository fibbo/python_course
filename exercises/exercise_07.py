"""Price summary exercise.

Calculate the total and the average of a list of prices and print a short summary.
"""


def total_price(prices):
    total = 0
    for price in prices:
        total += price
    return total


def average_price(prices):
    if len(prices) == 0:
        return "No average possible, list is empty."
    return total_price(prices) / len(prices)


def print_summary(prices):
    total = total_price(prices)
    average = average_price(prices)
    print(f"{len(prices)} items, total: {total}, average: {average:.2f}")


prices = [20.4, 4.5, 7]
print(total_price(prices))
print(average_price(prices))
print_summary(prices)
