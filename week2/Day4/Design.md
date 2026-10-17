## Library system ##

## What the system does. ##

Library Tracking: The system tracks books along with their total copies and how many are currently checked out (out).

Availability Rule: A book can only be borrowed if available copies exist (total - out > 0). Borrowing fails only when all copies are already checked out (out == total).

## Data model ##

-A library has: title,total,out.
-The dictionary key is the cleaned lowercase name.

**Example** 

library = {
    "python 101": {"total":5,"out":1},
    "programing cheat codes": {"total":7,"out":3}
}

## Add_book function (What it takes,returns and what could go wrong) ##

**Add_book(library,title,copies)** : returns (True/False , "message").

**What could go wrong**

-User may try to add an empty title input. `return False, "Enter book title Please."` *Nothing is stored.*

-User may try to add a book(title) that already exists. `return False, "Book already exists enter another book."` *The existing book isn't changed*

-User may try to add a negative number or 0 `eg (-1) or (0)` for copies. `return False, "Enter valid number of copies."` *Nothing is stored.*

-If every detail is correct:
library[title] = {
    "total":copies,"out":0
}
`return True, "Book add succesfull."`

## borrow_book - func What it takes,returns and what could go wrong ##

**borrow_book(library,title)** : returns (True/False), "message"

**What could go wrong** 

User may enter empty title input. `return False, "Enter book title please."` . Nothing changes.

-User may try to borrow a book that doesn't exist. `return False, "Sorry the book doesn't exist."`. Nothing changes.

-User may try to borrow when there's only one copy remaining or no copies remaining. `return False, "Borrow limit reached."` Nothing changes.

After succesfull borrow 
library[title]["out"] += 1

return True, "Book borrowed successfully."




