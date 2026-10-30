import math

eng2de = dict(one=1, two=2)


inventory = {"apples": [430, 23, 4], "bananas": 312}
for fruit, count in inventory.items():
    print(f"{fruit}: {count}")
    print(type(fruit), type(count))
# apples: 430
# bananas: 312
