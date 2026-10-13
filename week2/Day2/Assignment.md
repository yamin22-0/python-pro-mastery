Week 2, Day 2: Grade Book

New idea: a dictionary whose values are lists, passed into functions. You already used both separately (the wallet’s users dictionary, and lists in the shopping list). Here they work together. Here it is on different data:

python
stock = {"rice": [10, 5], "beans": []}      # each key holds a LIST

stock["rice"].append(8)                      # add to the list inside
print(stock["rice"])                         # [10, 5, 8]
print(sum(stock["rice"]) / len(stock["rice"]))   # average of the list

def add_item(stock, name):                   # the dictionary is passed in
    if name in stock:
        return "Already exists."
    stock[name] = []                         # a new empty list for this item
    return "Item added."

Changing the dictionary inside a function changes the original too, so you don’t need to return it.

The problem in plain English: a grade book that keeps students and their marks. The main part shows a menu: add a student, add a mark to a student, show a student’s average, show the best student, quit.

Write these four functions. Each does one job and prints nothing:

add_student(grades, name): returns a message. It rejects an empty or duplicate name (names cleaned with .strip().lower()).
add_mark(grades, name, mark): returns a message. The student must exist, and the mark must be a whole number from 0 to 100.
get_average(grades, name): returns the average, or None if the student doesn’t exist or has no marks yet.
best_student(grades): returns the name with the highest average. This is the find_largest pattern, so remember the best so far. It returns None if nobody has marks.

The main part prints the messages and results.

Example: add amina with marks 70 and 90 (average 80), and brian with 60 (average 60). best_student returns amina.

Do it in this order:

In Week2/Day2, write DESIGN.md. New today: a short data model section. List the things the program keeps (a student, a mark), the fields of each, and the relationship between them (one student has many marks). Write the example dictionary, like {"amina": [70, 90], "brian": [60]}, and say what the key is and what the value is. Also include one line per function: what goes in, what comes out. Send me the design note before you code.
Write the TODO comments, then code one function at a time, testing each alone before building the menu.
Test with the example, plus a duplicate student, a mark of 101, a mark of abc, adding a mark to a student who doesn’t exist, and get_average for a student with no marks.
DSA (30-40 minutes, by yourself)

Running Sum of 1d Array: given [1, 2, 3, 4], return [1, 3, 6, 10], where each item is the sum of everything up to and including that position.

Use the five steps:

Write the example by hand.
Solve it by hand, and notice what you remember as you go.
Write plain-English comments.
Code under them.
Test a normal list, [5], and [3, -1, 2].