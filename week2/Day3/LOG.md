## What built today ##

Today i built an inventory system where it keeps track of items added,items sold or to sell, It keeps items with a quantity and a price. It can add an item, sell an item, work out the total value of the stock, and list the items that are low.It has 4 functions and 17 tests (tested with pytest).

## What learnt today ##

Learnt *pytest* which is used for testing with real data.You create
the main file then you create a file to test it import the main file to this testing file and run `pytest folder/file_test.py`.If the test has errors it returns error but if all pass it returns the amount of tests passed as small dots`(...)`.

Learnt *Nested dictionaries:* which is how to structure and access a dictionary inside a dictionary.

Learnt *.items():* - Using for loop with `.items()` gives the key and value, and `.values()` gives the value pair only. 

Learnt *Reading failures:* In `assert a == b`, the left side (`a`) is what your function actually returned, helping you debug.

*Test value:* A test that can't fail proves nothing; tests must be strict enough to catch real mistakes.



## What confused me ##

Not using `test` when defining function in `test.py` which made the test skip testing the functions that don't start with test.

A test I changed on purpose to expect the wrong number failed with assert 1470 == 1471. That showed the function was right and the test was what I’d changed.

Plain pytest couldn’t find my tools until I ran source .../.venv/bin/activate first.

