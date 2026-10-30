numbers = list(range(1, 101))

index = 0
while index < len(numbers):
    number = numbers[index]
    # The FizzBuzz case has to be checked first, otherwise 15 would only print Fizz
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    index = index + 1
