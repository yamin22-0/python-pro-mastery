## What system built today ## 
Today i built a contact book where a user enters name , and phone number and it's stored in a dictionary.later the user can find a contact,delete and get shown all contacts.

## What learnt today ##

Learnt `dictionaries` which is how to store keys`name` and value`phone number`

Learnt `del` which is a built in keyword statement in python that is used for deletions.

Learnt `break` and `continue` - break stops the loop while continue skips the current iteration and jumps back to the top of loop.

## What confused me and how solved ## 

-I was confused about how `break` and `continue` affect loop execution in the `Add Contact` feature:
-Using `break` inside the input checks was unexpectedly killing the entire program loop.
-Using `continue` without proper checks was skipping the lines where contacts were saved to the dictionary.
**Solution:** I traced the code line-by-line and structured the validation so that invalid inputs trigger `continue` (returning the user safely to the menu prompt), while valid inputs allow the execution to reach the dictionary assignment step before cycling back.