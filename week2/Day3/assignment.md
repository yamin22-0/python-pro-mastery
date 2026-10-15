Today: Day 3, Inventory (clearer version)

Today you start with the design already prepared (the first line below), because you haven’t had an evening to write it. From tomorrow, you write your own the night before.

The goal: a few functions that keep a shop’s items, with pytest tests for each.

The data. One dictionary: the key is the item name, and the value is another dictionary with the quantity and the price.

python
inventory = {
    "rice":  {"qty": 10, "price": 120},
    "beans": {"qty": 3,  "price": 90},
}

To read the inner values: inventory["rice"]["qty"] gives 10. (This is a dictionary inside a dictionary: the first ["rice"] picks the item, and the second ["qty"] picks a field of that item.)

Rules for all functions: they print nothing, and they return a tuple (True, "message") or (False, "message"). Clean names with .strip().lower().

Part A (do this first, with its tests)

1. add_item(inventory, name, qty, price)

Rejects an empty name, a name that already exists, a quantity below 0, and a price of 0 or below.
On success, it stores {"qty": qty, "price": price} under the cleaned name.

2. total_value(inventory)

Returns one number: the sum of qty * price for every item.
An empty inventory gives 0.

Tests for Part A:

Test	Expected
add rice, 10, 120	True
add rice again	False
add (empty name)	False
add tea, -1, 50	False
add tea, 5, 0	False
total of the example above	1470
total of {}	0
Part B (only after Part A passes)

3. sell_item(inventory, name, qty)

The item must exist, and qty must be above 0.
You can’t sell more than is in stock.
On success, the stock goes down by qty.

4. low_stock(inventory, limit)

Returns a list of names whose qty is at or below the limit.

Tests for Part B:

Test	Expected
sell 4 rice from the example	True, and rice qty is now 6
sell 99 rice	False, and rice qty is unchanged
sell milk (doesn’t exist)	False
sell 0 rice	False
low_stock(example, 5)	["beans"]
low_stock(example, 1)	[]
How to work
Create inventory.py and test_inventory.py in Week2/Day3.
Write one function, then its tests, and run pytest. Don’t write the next function until the dots are green.
Test pattern:
python
from inventory import add_item

def test_add_item_good():
    inventory = {}
    result = add_item(inventory, "rice", 10, 120)
    assert result[0] == True

result[0] is the first part of the tuple, so it’s the True or False. Create a fresh inventory = {} inside each test, so tests don’t affect each other.

Today’s design: write only one short section in DESIGN.md: “What can go wrong”, with the rules from Part A and Part B in your own words. Everything else is above.