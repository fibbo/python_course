words = ["Python", "Java", "C", "Go", "JavaScript"]
min_word_length = 4

counter = 0
for word in words:
    if len(word) >= min_word_length:
        counter = counter + 1
        print(word)

print(f"{counter} of {len(words)} words are at least {min_word_length} characters long")
