Week 3, Day 3: Bills Reminder (modules and datetime)

Write the DESIGN.md this evening. Tomorrow morning, review it once, then code.

The goal: a small tracker for bills (rent, electricity, school fees) that tells you which are overdue and which are due soon. It’s built from two files that import each other, and it works with real dates.

New tools

1.Dates with datetime. It’s built in, so there’s nothing to install:

python
from datetime import date, datetime

exam = date(2026, 12, 1)                 # year, month, day
today = date(2026, 11, 20)

print(exam > today)                      # True: dates can be compared
print((exam - today).days)               # 11: subtracting gives a gap, .days is the number

2.Turning typed text into a date. strptime reads text in a format you describe, and raises ValueError if it doesn’t fit:

python
text = "2026-12-01"
parsed = datetime.strptime(text, "%Y-%m-%d").date()
print(parsed)                            # 2026-12-01

%Y is the year, %m the month, %d the day. Try "2026-13-01" and "hello" in practice.py, and read the errors.

3.Don’t call date.today() inside your functions. Then a test would give a different answer every day. Instead, pass today in as a parameter, so a test can say “pretend today is 20 November 2026”.

4.Modules: your own files that import each other. Put some functions in dates_helper.py. In another file in the same folder:

python
from dates_helper import parse_date, days_until
The data

A dictionary: the key is the cleaned lowercase bill name, and the value holds the amount and the due date. The date is stored as text and turned into a real date only when you compare.

python
bills = {
    "rent": {"amount": 15000, "due": "2026-11-05"},
    "electricity": {"amount": 2300, "due": "2026-11-28"},
}
The functions

Nothing prints. Dates are written YYYY-MM-DD.

File 1: dates_helper.py (Part A, with its tests first)

parse_date(text): returns a real date. It raises ValueError with a clear message if the text is empty, in the wrong format, or not a real date (month 13, or 30 February).
days_until(due, today): takes two real dates and returns a whole number of days from today to the due date. It’s negative if the due date has passed, and 0 if it’s due today.

File 2: bills.py (Part B, after Part A is green; it imports from dates_helper)
3.add_bill(bills, name, amount, due_text): returns (True/False, "message"). It rejects an empty name, a name that already exists, an amount of 0 or below, and a bad date (use parse_date and catch its ValueError). Nothing changes on a failure. On success, it stores the amount and the due date as text.
4.overdue_bills(bills, today): returns a list of bill names due before today. A bill due today is not overdue.
5.due_soon(bills, today, days): returns a list of bill names due from today up to days days from now, including today and the last day. Overdue bills are not included.

Tests to write

Use a fixed date in the tests, for example today = date(2026, 11, 20).

Function	Test	Expected
parse_date	"2026-11-05"	date(2026, 11, 5)
	" 2026-11-05 "	date(2026, 11, 5)
	"", "hello", "05-11-2026", "2026-13-01", "2026-02-30"	each raises ValueError
days_until	due 2026-11-25, today 2026-11-20	5
	due the same day as today	0
	due 2026-11-15, today 2026-11-20	-5
add_bill	good bill	True, and the stored due date is still text
	duplicate name	False, original unchanged
	empty name, amount 0, bad date	each False, and bills unchanged
	" RENT "	True, and "rent" is the key
overdue_bills	due yesterday	in the list
	due today (boundary)	not in the list
	no bills	[]
due_soon	due in exactly days days (boundary)	in the list
	due in days + 1 days	not in the list
	due today	in the list
	overdue bill	not in the list
What to write in DESIGN.md tonight (about 15 minutes)
What it does: one sentence.
Data model: the example above, and what the key and value are.
Why the date is stored as text: write the reason.
The two files: which functions go in dates_helper.py and which in bills.py, and why they’re separate.
One line per function: takes ___, returns ___, or raises ___.
Decisions: a bill due today is not overdue but is due soon, and today’s date is always passed in, never read inside a function.

Write each function’s “what can go wrong” right before you code it. Send me the note if you’d like me to check it.

DSA, after the assignment is done (30 minutes, by yourself)

Balanced Brackets, first version: a string of only ( and ). Return True if every ( has a matching ) in the right order. "(())" gives True, "(()" gives False, and ")(" gives False.

By hand, what do you need to remember as you go along the string? The string ")(" shows that the count alone isn’t enough, because the order matters. A running count that must never go below 0, and must end at exactly 0, is enough for this version. Test "(())", "(()", ")(", "()()" and "", predicting first.

Twist, only after that works: the string can also have [] and {}, like "([{}])" (True) and "([)]" (False). A count won’t work any more. You’ll need a stack: a list where you add with .append() and take the last one off with .pop(). I’ll teach it when you get there, so don’t look it up yet.
