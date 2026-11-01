## Bills reminder system ##

## What the system does ##

A small tracking system for bills that can add bills, shows bills that are due soon  and bills that are over due.

## Data model ##

-A dictionary of bills that show bill(name) and amount and due date.
-Name(key) is cleaned using `.strip()` and `.lower()`.


**Example**

bills = {
    "rent": {"amount":15000, "due":"2026-11-05"},
    "electricity": {"amount":2300,"due":"2026-11-07"}
}

File A *dates_helper.py*

## parse_date(text) what it takes,returns and what could go wrong. ## 

**parse_date(text)** - takes in a string representing date and returns
clean date in YYYY-MM-DD format.

**What could go wrong**

-User may try to leave text empty. `raises ValueError, "Please enter a date."`

-User may try to enter wrong date eg month 13 or february 30. `raises ValueError, "Please enter a valid date as YYYY-MM-DD."`

-User may try to enter date in wrong format. `raises ValuError, "Please enter a valid date as YYYY-MM-DD."`

on success returns the date as YYYY-MM-DD.

## days_until(due, today)  what it takes,returns and what could go wrong. ## 

**days_until(due, today)** takes in todays date and due date and returns a whole number of the differnce between today's date and due date.- negative number if todays date has already passed due date.returns 0 if todays date is the due date.

## add_bill(bills,name,amount,due_text) what it takes,returns and what could go wrong. ## 

**add_bill(bills,name,amount,due_text)** - takes in bills dictionary, name, amount and due as text. `returns True, "message or returns True, "message"`.
-Clean name using .strip().lower()

**What could go wrong**

-User may try to leave text empty. `return False, "Please enter a name."` *Nothing cahnges*

-User may try to enter a user that already exixts. `return False, "User already exists."` *Nothing cahnges*

-User may try to enter amount thats 0 or less than 0. `return False, "Please enter a valid amount."` *Nothing cahnges*

-User may try to enter a bad date. *Use try except to catch valueerror.*
`raises ValueError("Please enter valid date.")` *Nothing cahnges*

on success:
    bills[name] = {"amount":amount,"due_text":parsed_date.isoformat()}
    `return True, "Bill added successfully."`

