from library import add_book,borrow_book,return_book,available_books

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

def test_return_book_good():

    library = {"css mastery": {"total":3,"out":2}}

    result = return_book(library,"css mastery")
    assert result[0] == True
    assert result[1] == "Thank you for safely returning this book."
    assert library["css mastery"]["out"] == 1

def test_return_book_boundary():

    library = {"business": {"total":2,"out":1}}

    result = return_book(library,"business")
    assert result[0] == True
    assert library["business"]["out"] == 0

def test_return_book_nothing_out():

    library = {"math": {"total":10,"out":0}}

    result = return_book(library,"math")
    assert result[0] == False
    assert library["math"]["out"] == 0

def test_return_book_missing_book():

    library = {"hadith": {"total":6,"out":4}}

    result = return_book(library,"tafseer")
    assert result[0] == False
    assert "tafseer" not in library
    assert library["hadith"]["out"] == 4

def test_return_book_empty_title():

    library = {"geology": {"total":7,"out":3}}

    result = return_book(library," ")
    assert result[0] == False
    assert result[1] == "Enter book title please."
    assert library["geology"]["out"] == 3

def test_return_book_title_cleaning():

    library = {"economics": {"total":6,"out":4}}

    result = return_book(library," ECONOMICS ")
    assert result[0] == True
    assert "economics" in library
    assert " ECONOMICS " not in library
    assert library["economics"]["out"] == 3

def test_available_books_mixed():

    library = {"python 101": {"total": 3, "out": 1}, 
               "kenya history": {"total": 2, "out": 2}}

    result = available_books(library)
    assert result == ["python 101"]

def test_available_books_last_copy():

    library = {"think big": {"total":3,"out":2}}

    result = available_books(library)
    assert result == ["think big"]

def test_available_books_all_out():

    library = {"80-20 principle": {"total":8,"out":8}}

    result = available_books(library)
    assert result == []

def test_available_books_nothing_borrowed():

    library = {"kaizen methods": {"total":9,"out":0}}

    result = available_books(library)
    assert result == ["kaizen methods"]

def test_available_books_empty_library():

    library = {}

    result = available_books(library)
    assert result == []
