import json
from pathlib import Path

address_book = {}

while True:
    name = input("Enter name or type exit to quit: ")
    if name == "exit":
        break
    phone_number = input("Phone: ")
    address_book[name] = phone_number

path = Path("address_book.txt")
path.write_text(json.dumps(address_book, indent=2))
