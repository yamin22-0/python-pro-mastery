Day 5: Contact Book

New tools: dictionaries as storage, in on a dictionary, .get(), del, and break. Here they are on different data:

python
stock = {}                       # an empty dictionary
stock["rice"] = 120              # add: key "rice", value 120
stock["beans"] = 90

print("rice" in stock)           # True: `in` checks the keys
print(stock.get("sugar"))        # None: .get() gives None instead of crashing
print(stock.get("rice"))         # 120

del stock["beans"]               # delete a key
print(len(stock))                # 1

for name in stock:               # looping a dictionary gives the keys
    print(name, stock[name])

while True:                      # a loop that runs until you break out of it
    answer = input("Quit? (y/n): ")
    if answer == "y":
        break                    # leaves the loop

stock["sugar"] on a missing key crashes, which is why you use in or .get() first.

The problem in plain English: a contact book that stores names and phone numbers. The program shows a menu and keeps going until the user chooses to quit:

Add a contact
Find a contact
Delete a contact
Show all contacts
Quit

Rules:

Names are cleaned with .strip().lower(), so "Amina" and " AMINA " are the same contact.
A phone number must be all digits and exactly 10 long. Anything else is rejected with a message.
Adding a name that already exists is rejected.
Finding or deleting a name that doesn't exist prints a message, with no crash.
"Show all" on an empty book prints a message that there are no contacts.
An invalid menu choice prints a message and shows the menu again.

Example: add amina / 0711111111, then find AMINA shows her number. Find brian says not found. Delete amina, then "show all" says the book is empty.

Do it in this order:

Create a Day5 folder and write DESIGN.md with the four questions. Include what the dictionary holds (what the key is and what the value is). Send me the design note before you code.
Write the TODO comments, then code one option at a time, and run after each. Start with just the menu and "Quit", then add the options one by one.
Test with the example, plus a duplicate name, a phone number with 9 digits, a phone number with letters, and an invalid menu choice.