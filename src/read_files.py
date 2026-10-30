"""Read data from a text file line by line.

Each line of data.txt holds a timestamp and a value separated by whitespace.
The lines are split and the parts are stored in two separate lists.
"""

from pathlib import Path

# file_path = Path("words.txt")
# if file_path.exists():
#     print(f"File exists: {file_path}")
# else:
#     print("File doesn't exist")


# print(file_path.absolute().resolve())


# moby_dick_text = file_path.read_text()
# print(moby_dick_text)


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
