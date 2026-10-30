# Bonus: no check for 15 is needed if the two words are collected in a string
numbers = list(range(1, 101))

index = 0
while index < len(numbers):
    number = numbers[index]
    output = ""
    if number % 3 == 0:
        output = output + "Fizz"
    if number % 5 == 0:
        output = output + "Buzz"
    if output == "":
        print(number)
    else:
        print(output)
    index = index + 1
