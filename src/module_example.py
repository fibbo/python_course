"""Modules let you use code from other files and from the standard library.

You can import a whole module with "import math" or only single names from it
with "from math import sin".

You can also import your own modules, for example the queue variable from the lists module.
"""

import math
from math import sin

from lists import queue

print(math.sqrt(16))
print(math.e)
print(sin(math.pi))

# Only the queue variable is imported, the prints inside lists.py don't run.
print(queue)
