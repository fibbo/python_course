import random

# For this to work install matplotlib: `python -m pip install matplotlib`
import matplotlib.pyplot as plt


def guesses_needed(target_number):
    lower = 1
    upper = 100
    guess = random.randrange(1, 101)
    counter = 1

    while guess != target_number:
        if guess > target_number:
            upper = guess - 1
        else:
            lower = guess + 1
        guess = (lower + upper) // 2
        counter += 1

    return counter


targets = list(range(1, 101))
averages = []
for target in targets:
    tries = []
    for _ in range(500):
        tries.append(guesses_needed(target))
    averages.append(sum(tries) / len(tries))

plt.plot(targets, averages)
plt.xlabel("Target number")
plt.ylabel("Average number of guesses")
plt.xticks(range(1, 101, 2))
plt.savefig("average_tries_vs_target_number.png")
plt.show()

print(sum(averages) / len(averages))
