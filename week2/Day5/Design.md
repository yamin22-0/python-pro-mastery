## Expense tracking system ##

## What the system does ##

It's an expense tracking system that can add expenses , gets total expenses , expenses per category and top category.

## Data model ##

-An expense has category and amount.
-Category is cleaned using `.strip()` and `.lower()`.

**Example**

expenses = [
    {"category":"food","amount":10000},
    {"category":"oil","amount":210},
    {"category":"food","amount":500}
]

## add_expense(expenses,category,amount) what it takes,returns and what could go wrong. ## 

**add_expense(expenses,category,amount)** returns (True, "message"), or (False, "message").

**What could go wrong**

-User may try to enter an empty category input. `return False, "Please enter category."` *Nothing changes.*

-User may try to enter an amount of 0 and below. `return False, "Please enter valid amount."` *Nothing changes.*

On correct details:
    expenses = [ "category":"food","amount":10000]
`return True, "Expenses tracked successfully."`


