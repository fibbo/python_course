import random

target_number = int(input("Please enter your target number: "))

# The number can still be anywhere in this range
lower = 1
upper = 100

guess = random.randrange(1, 101)
counter = 1

while guess != target_number:
    print(f"Guess {counter}: {guess}")
    if guess > target_number:
        upper = guess - 1
    else:
        lower = guess + 1
    # Guessing in the middle halves the remaining range with every step
    guess = (lower + upper) // 2
    counter += 1

print(f"The number is {guess}")
print(f"It took me {counter} guesses.")
