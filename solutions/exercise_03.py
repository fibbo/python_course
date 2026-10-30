total = 0
while True:
    entry = input("Enter a number (or 'done' to finish): ")
    if entry == "done":
        break
    total = total + float(entry)

print(total)
