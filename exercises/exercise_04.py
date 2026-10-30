numbers = list(range(1, 101))

index = 0
while index < len(numbers):
    n = numbers[index]
    string = ""
    if n % 3 == 0:
        string += "Fizz"
    if n % 5 == 0:
        string += "Buzz"

    if string == "":
        print(n)
    else:
        print(string)

    index += 1

    # if n % 15 == 0:
    #     print("FizzBuzz")
    # elif n % 3 == 0:
    #     print("Fizz")
    # elif n % 5 == 0:
    #     print("Buzz")
    # else:
    #     print(n)
