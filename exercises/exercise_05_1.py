programming_languages = [
    "Python",
    "Java",
    "C",
    "Go",
    "JavaScript",
    "Kotlin",
    "Pascal",
    "Fortran",
]

min_word_length = int(input("Specify the minimum word length you want to check for: "))

counter = 0
for language in programming_languages:
    if len(language) >= min_word_length:
        print(language)
        counter += 1

print(
    f"I've found {counter} languages that are at least {min_word_length} characters long."
)
