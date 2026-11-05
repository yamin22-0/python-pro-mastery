Duka Manager (review project)

A small shop manager that uses everything from Week 1 Day 1 to Week 3 Day 3. You build it yourself from this design, one function at a time, with pytest tests for each.

1. What it does

Duka Manager is a command-line program for a small shop (a duka). It:

keeps products and stock,
records sales, either cash or on credit,
tracks what each customer owes and lets them pay it off,
tracks bills (rent, electricity) and reminds you which are overdue or due soon,
gives reports: low stock, best seller, total owed, and a daily summary.

Everything is saved to one file, duka.json, and loaded again when the program starts.

2. Why this project: the review map
You learned	Where it appears here
input, float, int, try/except ValueError (Week 1)	the menu, and the validators
menu loop with while True, break, continue (Week 1)	main.py
.strip().lower() and cleaned names (Week 1)	every function that takes a name
partial search with in (Week 1, contact book)	find_products
functions that return, one job each (Week 2)	every function
checks first, change last (Week 2)	sell, pay_debt, restock, add_bill...
nested dictionary, list of dictionaries (Week 2)	data["products"], data["sales"]
a set for unique items (Week 2)	daily_summary (unique credit customers)
.get(key, 0) + 1 counting (Week 2)	units_by_product
"remember the best so far" (Week 2 DSA)	top_product
pytest, boundary tests, mutation checks (Week 2)	every module
JSON save and load, with open (Week 3 Day 1)	storage.py
a missing, empty or damaged file (Week 3 Day 2)	load_data
raise ValueError, pytest.raises (Week 3 Day 2)	validators.py
modules that import each other, datetime (Week 3 Day 3)	the file layout, bills, dates

Not in this project, on purpose: classes (Week 4), SQL (Week 5), APIs (Week 6).

3. Files
duka/
  validators.py     # turns typed text into clean values, or raises ValueError
  storage.py        # save_data, load_data, new_data
  shop.py           # products, sales, debts
  bills.py          # bills and reminders
  reports.py        # read-only reports
  main.py           # the menu; the ONLY file that prints, asks, or reads today's date
  test_validators.py
  test_storage.py
  test_shop.py
  test_bills.py
  test_reports.py

Import rules:

shop.py and bills.py import from validators.py.
reports.py imports nothing from the other logic files.
main.py imports everything.
Nothing imports main.py.
4. Data model

One dictionary, called data, with four parts:

python
data = {
    "products": {
        "milk":  {"qty": 20, "price": 60.0},
        "bread": {"qty": 8,  "price": 55.0},
    },
    "sales": [
        {"date": "2026-11-01", "product": "milk", "quantity": 2,
         "price": 60.0, "customer": ""},
        {"date": "2026-11-01", "product": "bread", "quantity": 1,
         "price": 55.0, "customer": "amina"},
    ],
    "debts": {"amina": 55.0},
    "bills": {
        "rent": {"amount": 15000.0, "due": "2026-11-05"},
    },
}

What each part is:

products: the key is the cleaned lowercase product name. The value holds the stock (qty, a whole number) and the price (a float).
sales: a list, one dictionary per sale, in the order they happened. The price is the price at the time of the sale, because the product's price may change later. customer is "" for a cash sale, or the cleaned customer name for a credit sale.
debts: the key is the cleaned customer name, and the value is how much they owe. A customer who owes nothing is not in the dictionary.
bills: the key is the cleaned bill name. The due date is stored as text (YYYY-MM-DD) and turned into a real date only when you compare.

An empty data is:

python
{"products": {}, "sales": [], "debts": {}, "bills": {}}

Decisions about the data:

Money is a float, rounded to 2 decimals whenever you add or multiply it. Floats can be slightly off (0.1 + 0.2), so always round(..., 2). A later week teaches a safer way to handle money.
A sale with a customer name is a credit sale. A sale with customer = "" is a cash sale.
Dates are stored as text, and today is passed in. Only main.py is allowed to read the real date, so tests always give the same answers.
5. Rules for every function
Functions that change data return (True, "message") or (False, "message").
A failed call changes nothing. Every check comes before the one line that changes data.
Functions never print and never ask for input. main.py does that.
Reports never change data.
Names are cleaned with .strip().lower() inside each function that takes a name.
Functions never call date.today(). Dates come in as parameters.
6. The functions
validators.py

clean_name(text)

Takes text. Returns it stripped and lowercase.

parse_amount(text)

Takes text. Returns a float above 0.
Raises ValueError with a clear message if the text is empty, isn't a number, is nan or inf, or is 0 or below.

parse_quantity(text)

Takes text. Returns a whole number above 0.
Raises ValueError if the text is empty, a word, a decimal ("2.5"), 0, or negative.

parse_date(text)

Takes text in the form YYYY-MM-DD. Returns a real date.
Raises ValueError if the text is empty, in the wrong format, or not a real date (month 13, 30 February).
storage.py

new_data()

Takes nothing. Returns a fresh empty data (section 4).

save_data(data, filename)

Writes data to the file as JSON, replacing what was there. Returns nothing.

load_data(filename)

Returns the saved data.
Returns new_data() if the file is missing, empty, or damaged.
Returns new_data() if the file holds valid JSON that is not a dictionary (for example a list).
If the dictionary is missing one of the four parts, add that part as empty, and keep the parts that are there.
shop.py

add_product(data, name, qty, price)

Takes already-converted values (qty an int, price a float).
Rejects: an empty name, a name that already exists, qty below 0 (a new product may start with 0 stock), a price of 0 or below.
On success, stores {"qty": qty, "price": price}.

restock(data, name, qty)

The product must exist, and qty must be above 0. On success, adds to the stock.

set_price(data, name, price)

The product must exist, and the price must be above 0. On success, replaces the price. Past sales keep their old price.

find_products(data, text)

Returns a list of product names that contain the cleaned text anywhere in the name.
An empty text returns []. No match returns [].

sell(data, name, qty, date_text, customer)

Rules, in this order: clean the name, the product must exist, qty must be above 0, qty must not be more than the stock, the date must be valid (use parse_date and pass on its message). Only then change anything.
On success: reduce the stock, append a sale record (with the product's current price and the date stored as YYYY-MM-DD), and if customer (cleaned) is not empty, add round(qty * price, 2) to data["debts"][customer].
Use .get(customer, 0) for a customer who isn't in debts yet.

pay_debt(data, customer, amount)

The customer must be in debts, the amount must be above 0, and it must not be more than they owe.
On success, subtract it and round to 2 decimals. If the balance is now exactly 0, remove the customer from debts.
bills.py

add_bill(data, name, amount, due_text)

Rejects: an empty name, a duplicate name, an amount of 0 or below, a bad date (pass on parse_date's message).
On success, stores {"amount": amount, "due": <date as YYYY-MM-DD text>}.

pay_bill(data, name)

The bill must exist. On success, removes it.

days_until(due, today)

Takes two real dates. Returns due minus today as a whole number of days (negative if it has passed).

overdue_bills(data, today)

Returns a list of bill names due before today. A bill due today is not overdue.

due_soon(data, today, days)

Returns a list of bill names due from today up to days days away, including today and the last day. Overdue bills are not included.
reports.py (read-only)

low_stock(data, limit)

Returns a list of product names whose qty is at or below limit.

stock_value(data)

Returns the total of qty * price over all products, rounded to 2 decimals. Empty gives 0.

total_owed(data)

Returns the sum of all debts, rounded to 2 decimals. Empty gives 0.

units_by_product(data)

Returns a dictionary of product to the total quantity sold, built with .get(key, 0) + quantity.

revenue_by_product(data)

Returns a dictionary of product to total money (quantity times the price stored in each sale, added up), rounded to 2 decimals.

top_product(data)

Returns the name of the product with the most units sold, or None if there are no sales.
On a tie, the product that appeared first in sales wins. Use units_by_product and the "best so far" pattern.

daily_summary(data, day)

day is a real date. Looks at the sales whose stored date equals day.isoformat().
Returns a dictionary: {"sales": count, "units": total quantity, "revenue": money, "credit_revenue": money from credit sales, "credit_customers": sorted list of unique customer names}.
Use a set to collect the unique customers, and return sorted(...) so tests are stable.
A day with no sales gives zeros and an empty list.
main.py
Loads duka.json when it starts, using load_data.
Reads today's date once, here and only here.
Shows a menu in a while True loop:
1. Add product        7. Customer pays debt
2. Restock            8. Add bill
3. Change price       9. Mark bill paid
4. Find product      10. Reminders (overdue and due in 7 days)
5. Sell (cash)       11. Reports
6. Sell on credit    12. Quit
For each choice: ask for input, convert it with the validators inside try/except ValueError, call one function, and print the message or result.
A bad conversion prints the error and returns to the menu. It never crashes.
After every successful change, call save_data.
An invalid menu choice prints a message and shows the menu again.
Quit asks for confirmation, as in the contact book.
7. What can go wrong (the cases to test)
Area	Cases
Typed input	empty, a word where a number is expected, a decimal where a whole number is expected, 0, negative, nan, inf, spaces around the text
Names	capitals and spaces (" MILK "), an empty name, a duplicate
Stock	selling more than the stock, selling exactly the stock (allowed), selling 0, a product that doesn't exist
Credit	a customer who isn't in debts yet, a customer who already owes, paying more than owed, paying exactly what is owed (customer removed)
Dates	the wrong format, month 13, 30 February, a leap day, a bill due today, due yesterday, due in exactly days, due in days + 1
Files	missing, empty, damaged, valid JSON that is a list, a dictionary with a missing part, a round trip (save then load)
Reports	an empty data, one sale, a tie for the top product, a day with no sales
8. Tests to write

Write the tests for each function before you trust it, using tmp_path for files and a fixed today = date(2026, 11, 20) for dates. Each test builds its own small data by hand.

Minimum for each function: the good case, each way it can fail (and check that data is unchanged), a cleaning case, and each boundary.

Mutation checks to run (predict which tests fail, then put each change back):

sell: change the stock check from > to >=.
sell: delete the line that adds to debts.
pay_debt: delete the "remove at exactly 0" lines.
load_data: catch only FileNotFoundError.
overdue_bills: change < 0 to <= 0.
due_soon: change 0 <= to -100 <=.
top_product: change > to >= (the tie test must fail).
parse_quantity: delete the check for decimals.
9. Build order

Finish each milestone with green pytest and a commit before starting the next.

Milestone	What	Commit message
M1	validators.py and storage.py with their tests	review-m1: validators and storage
M2	add_product, restock, set_price, find_products, sell with tests	review-m2: products and sales
M3	pay_debt and bills.py with tests	review-m3: debts and bills
M4	reports.py with tests	review-m4: reports
M5	main.py, a README, a full manual run through the menu	review-m5: menu and readme

A realistic pace is one milestone a day, so about five working days. Work the way you always do: write a function's rules, code it, test it, tick it off.

10. How you will know you understood

You understood the material if you can do these without looking at old code:

 Write each function from your own plain-English comments.
 Say why every check comes before the line that changes data.
 Explain why today is passed in and date.today() appears only in main.py.
 Explain why load_data returns new_data() for three different kinds of bad file.
 Explain why a sale stores its own price.
 Predict which tests fail for each mutation check, before running it.
 Read a pytest failure from the bottom up and say what is wrong.
 Run the whole menu by hand with bad input and see no crash.

Anything you can't do is the next thing to practise. That is the point of this project.

11. Rules for this project
You write the code. No AI-written code, including from me. If you get stuck, send your plain-English comments and say which step stopped you (after trying for 20 minutes).
Reuse your own code from Week 2 and Week 3, but be able to explain every line. If you can't, rewrite it from the comments.
Keep a LOG.md, in your own words: what you built, what confused you (with the real error), a design decision, and the mutation checks.
Add to your "bugs I repeat" list as you go.