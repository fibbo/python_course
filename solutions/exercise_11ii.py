import json
from pathlib import Path

path = Path("address_book.txt")

address_book = {}
# On the very first run the file does not exist yet
if path.exists():
    address_book = json.loads(path.read_text())


def insert_person():
    name = input("Please enter a name: ")
    phone_number = input("Please enter a phone number: ")
    address_book[name] = phone_number


def search_person():
    name = input("Please provide the name of the person: ")
    if name in address_book:
        print(f"The phone number of {name} is: {address_book[name]}")
    else:
        print("Person not found")


def remove_person():
    name = input("Please provide the name of the person you want to remove: ")
    if name in address_book:
        del address_book[name]
        print(f"Successfully removed {name}")
    else:
        print("Person not found")


print("What do you want to do?")
print("Enter 'add' to add a new person to the address book")
print("Enter 'search' to lookup a phone number")
print("Enter 'remove' to remove a person from the address book")
print("Enter 'exit' to quit")

while True:
    action = input(">>> ")
    if action == "add":
        insert_person()
    elif action == "search":
        search_person()
    elif action == "remove":
        remove_person()
    elif action == "exit":
        break
    else:
        print(f"'{action}' is not one of add, search, remove, exit")

print("Bye Bye")

path.write_text(json.dumps(address_book, indent=2))
