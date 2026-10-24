Week 3, Day 1: Debt Book (save and load with JSON)

The goal: a small shop “debt book” that keeps what each customer owes, and remembers it after the program closes. Until now, everything vanished when a program ended. Today the data goes into a file.

The new tools

1. Saving a dictionary to a file. Here it is on different data:

python
import json

prices = {"milk": 60, "bread": 55}

with open("prices.json", "w") as f:     # "w" means write
    json.dump(prices, f)                # puts the dictionary into the file

with open("prices.json") as f:          # no letter means read
    loaded = json.load(f)               # gives the dictionary back

print(loaded)                           # {'milk': 60, 'bread': 55}
with open(...) as f: opens the file and closes it for you when the block ends.
json.dump(data, f) writes. json.load(f) reads.
Run it, then open prices.json in VS Code. It’s plain text, and you can read it.

2. A file that doesn’t exist yet. The first time the program runs, there is no file, and open would crash. Today’s simple check:

python
import os

if not os.path.exists("prices.json"):
    return {}

(Day 2 teaches a better way, with try/except.)

3. Testing without touching real files. pytest gives every test a free temporary folder if you add tmp_path as a parameter:

python
def test_example(tmp_path):
    filename = tmp_path / "prices.json"     # a file inside a temporary folder

It’s deleted afterwards, so your tests never overwrite your real data.

The data

A dictionary: the key is the cleaned lowercase customer name, and the value is the amount they owe.

python
debts = {"amina": 500, "brian": 300}
The functions

Clean names with .strip().lower(). Nothing prints. The first two return (True/False, "message").

Part A (do this first, with its tests)

add_debt(debts, name, amount): rejects an empty name and an amount of 0 or below. If the customer is new, it creates them with that amount. If they already exist, it adds to what they owe.
total_owed(debts): returns one number, the sum of everything owed. An empty book gives 0.

Part B (only after Part A is green)
3. pay_debt(debts, name, amount): the customer must exist, the amount must be above 0, and it can’t be more than they owe. On success, subtract it. When the balance reaches exactly 0, remove the customer from the dictionary.

Part C (only after Part B is green)
4. save_debts(debts, filename): writes the dictionary to the file. It returns nothing.
5. load_debts(filename): reads the file and returns the dictionary. If the file doesn’t exist, it returns {}.

Tests to write
Function	Test	Expected
add_debt	new customer amina, 500	True, and debts == {"amina": 500}
	add 300 more for amina	True, and her total is 800
	empty name	False, and debts == {}
	amount 0	False, and debts == {}
	" AMINA "	True, and "amina" is the key
total_owed	{"amina": 500, "brian": 300}	800
	{}	0
pay_debt	pay 200 of 500	True, and the balance is 300
	pay exactly 500 of 500 (boundary)	True, and "amina" not in debts
	pay 501 of 500	False, and the balance is still 500
	customer not in the book	False
	amount 0	False, and the balance is unchanged
save and load	save, then load	the same dictionary comes back
	load a file that doesn’t exist	{}

For the save and load tests, use tmp_path, as shown above.

What to write in DESIGN.md now (about 15 minutes)
What it does: one sentence.
Data model: the example dictionary, and what the key and the value are.
What is saved: the file name (debts.json) and what the file contains. Copy what a file looks like for the example above. This is the new design skill for this week: say what is saved, where, and in what format.
One line per function: takes ___, returns ___.
Decisions: what happens when a balance reaches 0 (the customer is removed), and what load_debts returns when there’s no file.

Write each function’s “what can go wrong” right before you code it, as you did last week.

Send me the note if you’d like me to check it before you code. When you code, follow your cycle: plain-English comments, the function, its tests, and green before the next function.

DSA, after the assignment is done (30 minutes, by yourself)

Two Sum: given a list of numbers and a target, return the positions of the two numbers that add up to the target. Example: [2, 7, 11, 15] with target 9 gives [0, 1], because 2 + 7 is 9.

By hand, as you go along the list, what do you need to remember so that for each new number you can instantly ask “is the number I need already behind me?” You’ve used a dictionary and a set for this kind of question before. Test the example, a case where the pair is at the end, and a case with negative numbers, and predict first.