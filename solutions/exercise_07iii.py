def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


def average_price(prices):
    return total_price(prices) / len(prices)


def print_summary(prices):
    total = total_price(prices)
    average = average_price(prices)
    print(f"{len(prices)} items, total {total:.2f}, average {average:.2f}")


prices = [4.50, 2.00, 13.90]
print_summary(prices)
