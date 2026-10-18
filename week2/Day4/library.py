#TODO: PART A :
#TODO: Validate for add_book(library,title,copies) function if book title is empty,there;s an existing copy of that book and if the number of copies is either negative number or 0.
#TODO: Validate for borrow_book(library,title) - function if a book title is empty,if the book is in the system and if the books aren't at the limit of being borrowed.
#TODO: Validate for retrurn_book(library,title) - function if a book title is empty,if the book is in the system and if the user isn't trying to return a book that was never borrowed in the first place.

def add_book(library,title,copies):

    title = title.strip().lower()

    if not title:
        return False, "Enter book title please."
    elif title in library:
        return False, "Book already exists."
    elif copies <= 0:
        return False, "Enter valid number of copies."
    else:
        library[title] = {"total":copies,"out":0}
        return True, "Book add successfull."

def borrow_book(library,title):

    title = title.strip().lower()

    if not title:
        return False, "Enter book title please."
    elif title not in library:
        return False, "Sorry, Book doesn't exist."
    elif library[title]["out"] >= library[title]["total"]:
        return False, "Borrow limit reached."
    else:
        library[title]["out"] += 1
        return True, "Book borrowed successfully."

def return_book(library,title):

    title = title.strip().lower()

    if not title:
        return False, "Enter book title please."
    elif title not in library:
        return False, "Sorry, Book doesn't exist."
    elif library[title]["out"] <= 0:
        return  False, "Can only return books borrowed."
    else:
        library[title]["out"] -= 1
        return True, "Thank you for safely returning this book."

def available_books(library):

    available = []

    for title,item in library.items():
        if item["out"] < item["total"]:
            available.append(title)

    return available

