"""In this file we will create a dictionary from a file.

The file contains English words and their German translations as JSON, written by
serialize_dictionary.py. It looks like this:

{"one": "eins", "two": "zwei"}
"""

import json
from pathlib import Path

# Proving that the dictionary is empty before reading the file
dictionary = {}

print(dictionary)

dictionary_file = Path("dictionary.txt")
dictionary = json.loads(dictionary_file.read_text())


for eng, de in dictionary.items():
    print(eng, de)
