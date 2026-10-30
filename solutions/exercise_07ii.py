def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


def average_price(prices):
    return total_price(prices) / len(prices)


prices = [4.50, 2.00, 13.90]
print(average_price(prices))
