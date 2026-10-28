Week 3, Day 2: Safe Price List (errors that don’t crash)

Write the DESIGN.md this evening. Tomorrow morning you review it once and start coding.

The goal: a small shop price list that doesn’t crash when the input is bad, or when the file is missing, empty or damaged. Yesterday, a damaged debts.json would have crashed json.load. Today you handle that.

New tools

1. try / except with a named error. You’ve used it for ValueError. The pattern is the same for other errors:

python
try:
    age = int(text)
except ValueError:
    age = 0

Name the specific error you expect. A bare except: hides real bugs.

2. Handling a missing file with try instead of os.path.exists. On a different example:

python
import json

try:
    with open("notes.json") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = {}

3. A file that exists but is empty or damaged. json.load raises json.JSONDecodeError when the text isn’t valid JSON. You can catch two errors in one try:

python
except (FileNotFoundError, json.JSONDecodeError):
    notes = {}

4. raise: a function refusing bad input. Instead of returning (False, "..."), a function can stop and raise an error that the caller handles:

python
def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        raise ValueError("Age must be a whole number")
    if age < 0:
        raise ValueError("Age can't be negative")
    return age

5. Testing that a function raises, with pytest:

python
import pytest

def test_bad_age():
    with pytest.raises(ValueError):
        parse_age("abc")

The test passes only if the error is raised.

6. Writing a damaged file for a test. tmp_path gives you a temporary folder, and .write_text() puts text in a file:

python
filename = tmp_path / "prices.json"
filename.write_text("this is not json")
The data

A dictionary: the key is the cleaned lowercase product name, and the value is the price (a float).

python
prices = {"milk": 60.0, "bread": 55.0}
The functions

Nothing prints. Clean names with .strip().lower().

Part A (do this first, with its tests)

parse_amount(text): takes the text a user typed, and returns a float above 0. It raises ValueError with a clear message if the text is empty, isn’t a number, or is 0 or below.

Part B (after Part A is green)
2. save_prices(prices, filename): writes the dictionary to the file. It returns nothing.
3. load_prices(filename): returns the dictionary. If the file is missing, empty or damaged, it returns {}. Use try / except, with no os.path.exists.

Part C (after Part B is green)
4. set_price(prices, name, text): rejects an empty name. Calls parse_amount(text) and catches the ValueError. On success, it stores the price (replacing an old one) and returns (True, "message"). On failure, it returns (False, "message") and changes nothing.

Tests to write
Function	Test	Expected
parse_amount	"500"	500.0
	" 250.5 "	250.5
	"abc"	raises ValueError
	""	raises ValueError
	"0"	raises ValueError
	"-5"	raises ValueError
save_prices + load_prices	save, then load	the same dictionary
	missing file	{}
	file containing not json	{}
	empty file (write_text(""))	{}
set_price	"milk", "60"	True, and prices == {"milk": 60.0}
	change an existing price	True, and the new price replaces the old one
	"milk", "abc"	False, and prices unchanged
	"milk", "0"	False, and prices unchanged
	empty name	False, and prices unchanged
	" MILK ", "60"	True, and the key is "milk"
What to write in DESIGN.md tonight (about 15 minutes)
What it does: one sentence.
Data model: the example dictionary, and what the key and the value are.
What is saved: prices.json, and what the file looks like for the example.
One line per function: takes ___, returns ___, or raises ___.
Decisions: what load_prices returns for a missing file, an empty file and a damaged file (the same answer for all three, {}), and what parse_amount raises.

Write each function’s “what can go wrong” right before you code it, as before. Send me the note tonight if you’d like me to check it.

DSA, after the assignment is done (30 minutes, by yourself)

Valid Palindrome (two pointers): return True if a word reads the same forwards and backwards. "racecar" gives True, and "abca" gives False.

This is your first two pointers problem. By hand, put one finger at the first letter and one at the last. Compare them. If they match, move both fingers inward. If they ever differ, it’s False. Keep going until the fingers meet. You need two variables for the two fingers (for example left and right), and a while left < right: loop.

Test "racecar", "abca", "abba" (even length), "a", and "", predicting each first. Log two lines in DSA-LOG.md in your own words.