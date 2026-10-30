"""Serialize a dictionary to JSON and write it to a file.

json.dumps() turns the dictionary into a string, which is then written to
dictionary.txt.
"""

import json
from pathlib import Path

my_dict = {"one": "eins", "two": "zwei"}

my_dict_as_string = json.dumps(my_dict)
print(my_dict_as_string)

dictionary_file = Path("dictionary.txt")

with dictionary_file.open("w") as file:
    file.writelines(my_dict_as_string)
