Day 5, Expense Tracker

Write the DESIGN.md this evening, and review it in the morning before you code. DSA comes after the assignment is done.

The goal: four functions that keep a list of expenses, with pytest tests.

New idea: a list of dictionaries, and .get(key, 0). Each expense is a small dictionary, and all of them live in a list:

python
expenses = [
    {"category": "food", "amount": 200},
    {"category": "transport", "amount": 150},
    {"category": "food", "amount": 300},
]

And .get(key, 0) reads a value, giving 0 if the key doesn’t exist yet. Here it is on different data:

python
counts = {}
for word in ["a", "b", "a"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)       # {'a': 2, 'b': 1}

Rules for all functions: clean categories with .strip().lower(). Functions print nothing. add_expense returns (True/False, "message").

Part A

1.add_expense(expenses, category, amount): rejects an empty category and an amount of 0 or below. On success, it appends 
{"category": category, "amount": amount}.

2.total_spent(expenses): returns the sum of all amounts, or 0 if there are none.

Part B
3.spent_by_category(expenses): returns a dictionary of category to total. For the example above: {"food": 500, "transport": 150}.

4.top_category(expenses): returns the name of the category with the highest total, or None if there are no expenses. It uses spent_by_category, and it’s the same sticky-note pattern as best_student.

Tests (at least these):

Test	Expected
add food, 200	True, and the list has one expense
add (empty category)	False, and the list is empty
add food, 0	False, and the list is empty
add " FOOD ", 50	True, and the stored category is food
total_spent(example)	650
total_spent([])	0
spent_by_category(example)	{"food": 500, "transport": 150}
spent_by_category([])	{}
top_category(example)	"food"
top_category([])	None