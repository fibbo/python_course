"""In this file we will create a dictionary from a file.
The file will contain a list of words in English and their corresponding
translations in German. The file will be in the following format:
{
    "one": "eins",
    "two": "zwei",
}
"""

import json
from pathlib import Path

# Proving that the dictionary is empty before reading the file
dictionary = {}

print(dictionary)

dictionary_file = Path("dictionary.txt")
# dictionary = json.loads(dictionary_file.read_text())
with dictionary_file.open("r") as file:
    for line in file:
        dictionary = json.loads(line)


for eng, de in dictionary.items():
    print(eng, de)
