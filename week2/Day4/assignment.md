Tomorrow: Day 4, Library Books

Write DESIGN.md for this tonight, and review it tomorrow morning before you code. If you send me the note this evening, I’ll check it.

The goal: four functions that keep a library’s books and who has borrowed copies, with pytest tests.

The data: a dictionary where the key is the book title, and the value is a small dictionary of two counters.

python
library = {
    "python 101": {"total": 3, "out": 1},
    "kenya history": {"total": 2, "out": 2},
}

total is how many copies the library owns, and out is how many are currently borrowed. So available copies = total - out. (This is the same nested-dictionary shape as the inventory.)

Rules for all functions: clean titles with .strip().lower(). Functions print nothing, and return (True, "message") or (False, "message"), except available_books.

Part A

1.add_book(library, title, copies): rejects an empty title, a title that already exists, and copies below 1. On success it stores {"total": copies, "out": 0}.
2.borrow_book(library, title): the book must exist, and at least one copy must be available (out is less than total). On success, out goes up by 1.

Part B
3.return_book(library, title): the book must exist, and out must be above 0 (you can’t return a copy nobody borrowed). On success, out goes down by 1.
4.available_books(library): returns a list of titles that have at least one available copy.

Tests (at least these):

Test	Expected
add python 101, 3 copies	True, and total is 3, out is 0
add the same title again	False
add with 0 copies	False
borrow a book with copies available	True, and out goes up by 1
borrow kenya history (total 2, out 2)	False, and out is unchanged
borrow a book that doesn’t exist	False
return a book that is out	True, and out goes down by 1
return python 101 when out is 0	False
available_books on the example above	["python 101"]

The row for kenya history is the boundary: all copies are out, so it can’t be borrowed. For available_books, think about which check decides whether a title goes in the list, and look at how you wrote low_stock.