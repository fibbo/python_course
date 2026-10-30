def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


prices = [4.50, 2.00, 13.90]
print(total_price(prices))
