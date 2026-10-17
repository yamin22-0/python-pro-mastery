## Library system ##

## What the system does. ##

Keeps a library of books and how many copies are there,  It can add a book, borrow a book , return a book and check available books.
Out means the books that have been borrowed,Available copies equals to total - out,

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


