"""Write text to a file.

Opening the file in append mode ("a") adds the text to the end of the file
instead of overwriting it.
"""

from pathlib import Path


file_path = Path("note_book.log")

with file_path.open("a") as file:
    file.writelines("Test")
