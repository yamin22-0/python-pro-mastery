## Debt book system ##

## What the system does ##

A debt book system that adds debts,calculates total debts owed, payment of debt and saves the data.

## Data model ##

-debts has name and amount.
-Name(key) is cleaned using `.strip()` and `.lower()`.

**Example**

debts = {"amina":500, "binka":300 }

## add_debt(debts,name,amount) what it takes,returns and what could go wrong. ## 

**add_debts(debts,name,amount)** returns (True, "message"), or (False, "message").

**What could go wrong**

-User may try to enter an empty name input. `return False, "Please enter name."` *Nothing changes.*

-User may try to add an amount of 0 or below 0. `return False, "Please enter valid amount."` *Nothing changes.*

On correct details:
    debts[name] = debts.get(name, 0) + amount
`return True, "debt added."`

## total_owed(debts) what it takes,returns and what could go wrong. ## 

**total_owed(debts)** returns sum of the dictionary and for an empty dictionary returns 0.

## What is saved ##

**file name = debts.json**
**file contents**

`json {"amina":500,"binka":300}`
