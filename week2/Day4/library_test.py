from library import add_book,borrow_book

def test_add_book_good():

    library = {}
    title,total = "python 101",5
    
    result = add_book(library,title,total)
    assert result[0] == True
    assert result[1] == "Book add successfull."
    assert library["python 101"] == {"total":5,"out":0}

def test_add_book_duplicate():

    library = {}

    add_book(library,"kenyan history",10)

    result = add_book(library,"kenyan history",99)
    assert result[0] == False
    assert library["kenyan history"]["total"] == 10

def test_add_book_empty_title():

    library = {}

    result = add_book(library," ",3)
    assert result[0] == False
    assert library == {}

def test_add_book_zero_copies():

    library = {}

    result = add_book(library,"programming 001",0)
    assert result[0] == False
    assert "programming 001" not in library

def test_add_book_negative_copies():

    library = {}

    result = add_book(library,"master javascript",-9)
    assert result[0] == False
    assert "master javascript" not in library

def test_add_book_title_cleaning():

    library = {}

    result = add_book(library," ZOOLOGY ",7)
    assert result[0] == True
    assert "zoology" in library
    assert " ZOOLOGY " not in library


def test_add_book_boundary():

    library = {}

    result = add_book(library,"botany",1)
    assert result[0] == True
    assert library["botany"]["total"] == 1

def test_borrow_book_good():

    library = {"python 101": {"total":3,"out":1}}

    result = borrow_book(library,"python 101")
    assert result[0] == True
    assert result[1] == "Book borrowed successfully."
    assert library["python 101"]["out"] == 2

def test_borrow_book_last_copy():

    library = {"chemistry": {"total":2,"out":1}}

    result = borrow_book(library,"chemistry")
    assert result[0] == True
    assert library["chemistry"]["out"] == 2 

def test_borrow_book_non_available():

    library = {"mathematic": {"total":5,"out":5}}

    result = borrow_book(library,"mathematic")
    assert result[0] == False
    assert library["mathematic"]["out"] == 5

def test_borrow_book_missing_book():

    library = {"english aid": {"total":6,"out":0}}

    result = borrow_book(library,"tea")
    assert result[0] == False
    assert "tea" not in library
    assert library["english aid"]["out"] == 0

def test_borrow_book_empty_title():

    library = {"history": {"total":3,"out":2}}

    result = borrow_book(library," ")
    assert result[0] == False
    assert result[1] == "Enter book title please."
    assert library["history"]["out"] == 2

def test_borrow_book_title_cleaning():

    library = {"geography": {"total":2,"out":1}}

    result = borrow_book(library," GEOGRAPHY ")
    assert result[0] == True
    assert "geography" in library
    assert " GEOGRAPHY " not in library