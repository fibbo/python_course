"""FizzBuzz exercise
Showing two different ways to implement the FizzBuzz problem where one doesn't
explicitly check for 15 but assembles the output string based on the divisibility of 3 and 5.
"""


def fizz_buzz(numbers):
    index = 0
    while index < len(numbers):
        n = numbers[index]
        string = ""
        if n % 3 == 0:
            string += "Fizz"
        if n % 5 == 0:
            string += "Buzz"

        # This is equal to checking if string != ""
        if string:
            print(string)
        else:
            print(n)

        index += 1


def fizz_buzz_2(numbers):
    index = 0
    while index < len(numbers):
        n = numbers[index]
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

        index += 1


numbers = list(range(1, 101))
fizz_buzz(numbers)
fizz_buzz_2(numbers)
