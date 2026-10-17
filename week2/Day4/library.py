#TODO: PART A :
#TODO: Validate for add_book(library,title,copies) function if book title is empty,there;s an existing copy of that book and if the number of copies is either negative number or 0.


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

