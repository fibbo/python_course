"""Dictionaries store key-value pairs.

A dictionary maps each key to a value. You can create one with dict() or with curly
braces, and loop over its keys and values together with items().
"""

import math


eng2de = dict(one=1, two=2)


inventory = {"apples": [430, 23, 4], "bananas": 312}
for fruit, count in inventory.items():
    print(f"{fruit}: {count}")
    print(type(fruit), type(count))
# apples: 430
# bananas: 312
