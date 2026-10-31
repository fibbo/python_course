"""Read text files with pathlib.

exists() checks if a file is there before reading it, and read_text() reads the
whole file at once. For large files, open() lets you go through the file line by
line. Each line of data.txt holds a timestamp and a value, which are stored in two
separate lists.
"""

from pathlib import Path

file_path = Path("words.txt")
if file_path.exists():
    print(f"File exists: {file_path}")

    # You can also get the absolute path of the file with the resolve() method.
    print(file_path.absolute().resolve())

    # You can read the whole content of a file with the read_text() method.
    moby_dick_text = file_path.read_text()
    print(moby_dick_text)
else:
    print("File doesn't exist")


# If the file is large, you can read it line by line with the open() method
# and then iterate over the lines with a for loop. This is more memory efficient.
file_path = Path("data.txt")
timestamp = []
values = []
with file_path.open("r") as file:
    for line in file:
        line = line.strip()
        ts, val = line.split()
        timestamp.append(float(ts))
        values.append(val)

print(timestamp, values)
