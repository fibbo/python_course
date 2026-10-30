from pathlib import Path

min_word_length = 4
counter = 0
total = 0

file_path = Path("words.txt")
if file_path.exists():
    with file_path.open("r") as file:
        for line in file:
            word = line.strip()
            total += 1
            if len(word) >= min_word_length:
                counter += 1
                print(word)
    print(f"{counter} of {total} words are at least {min_word_length} characters long")
else:
    print("words.txt not found")
