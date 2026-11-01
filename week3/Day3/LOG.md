## Week 3, Day 3: Bills reminder ##

## What built today ##

-A bill reminder system that u can add bills then it reminds u if its over due or or due soon and handles errors so system doesn't crash. 

## What learnt today ##
-`datetime`: `date(2026, 11, 5)` turns string date into numbers so u can do arithmetics on it. 
-`strptime`: It turns string into actual date and it reject invalid dates.

-`.isoformat()`: it turns string into date format (YYYY-MM-DD) so add_bill function had a bills(dictionary) this `isoformat()` helps turn into date that can be stored inside dictionary. 

-Importing my own file: `from dates_helper import parse_date` - helps sharing logic of functions between 2 different files.


-Why `today` - for when testing u write today as a variable and then when asserting call the today in the parameter makes it easier for testing.

## What confused me, and how I fixed it ##

-`unsupported operand type(s) for -: 'datetime.date' and 'tuple'` - I passed a tuple instead of single parsed date.I fixed it by passing parsed date.

-`assert False == True` in the cleaning test, caused by my setup
I was passing key in the dictionary while i was trying to add another key i later emptied the dictionary to start empty.


## Design decision ##

Stored dates inside dictionary as clean `isoformat` and used `date` to make them real dates so they can handle calculations.

## Mutation checks
-**`<` to `<=` in `overdue_bills`**: 
  - **Failed tests:** `test_overdue_bills_today`, `test_overdue_bills_mixed`
  - **Error messages:** `AssertionError: assert ['water'] == []` and `AssertionError: assert ['fees', 'rent'] == ['fees']`
- **`<= days` to `< days` in `due_soon`**: 
-**Failed test:** Boundary check dropping the exact final day (e.g., day 7).
-**Error message:** `AssertionError: assert [] == ['water']` (Left list was empty).
- **`0 <=` to `0 <` in `due_soon`**: 
- **Failed tests:** `test_due_soon_due_today`, `test_due_soon_mixed`
-**Error message:** `AssertionError: assert ['water'] == ['rent', 'water']` (Missing today's bill).
- **`0 <=` to `-100 <=` in `due_soon`**: 
- **Failed tests:** `test_due_soon_due_over_due`, `test_due_soon_mixed`
-**Error messages:** `AssertionError: assert ['rent'] == []` and `AssertionError: assert ['rent', 'water', 'food'] == ['rent', 'water']`(Allowed overdue bills into the due-soon window).