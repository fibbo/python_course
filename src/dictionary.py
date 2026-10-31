"""Dictionaries store key-value pairs.

A dictionary maps each key to a value. You can create one with dict() or with curly
braces, and loop over its keys and values together with items().
"""

eng2de = {"one": "eins", "two": "zwei"}
print(eng2de)

# You could also create a dictionary with the dict() constructor, but this is less
# common because it is less readable and more verbose. For example, the following
# code creates the same dictionary as above:
# eng2de = dict(one="eins", two="zwei")

inventory = {"apples": [430, 23, 4], "bananas": 312}
for fruit, count in inventory.items():
    print(f"{fruit}: {count}")
    print(type(fruit), type(count))
# apples: [430, 23, 4]
# bananas: 312
