"""Modules let you use code from other files and from the standard library.

You can import a whole module with "import math" or only single names from it
with "from math import sin".
"""

import math
from math import sin
# from lists import queue

print(math.sqrt(16))

print(4 / 2)
print(4 + 2)

print(math.e)
print(sin(math.pi))


from pathlib import Path

file_path = Path("words.txt")


# print(queue)
