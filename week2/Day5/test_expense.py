from expense import add_expense,total_spent,spent_by_category,top_category

## tests for add_expense ##

def test_add_expense_good():

    expenses = []

    category,amount = "food",1000
    result = add_expense(expenses,category,amount)

    assert result[0] == True
    assert result[1] == "Expense tracked succesfully"
    assert expenses == [{"category":"food","amount":1000}]

def test_add_expense_empty_category():

    expenses = []
    result = add_expense(expenses," ",250)

    assert result[0] == False
    assert expenses == []

def test_add_expense_zero_amount():

    expenses = []
    result = add_expense(expenses,"oil",0)

    assert result[0] == False
    assert expenses == []

def test_add_expense_negative_amount():

    expenses = []
    result = add_expense(expenses,"oil",-100)

    assert result[0] == False
    assert expenses == []

def test_add_expense_cleaning():

    expenses = []
    result = add_expense(expenses," MAINTANANCE ",5000)

    assert result[0] == True
    assert expenses[0]["category"] == "maintanance"

def test_add_expenses_two_adds():

    expenses = []
    result1 = add_expense(expenses,"food",650)
    result2 = add_expense(expenses,"oil",100)

    assert result1[0] == True
    assert result2[0] == True
    assert len(expenses) == 2

## Tests for total_spent ##

def test_total_spent_multiple_expense():

    expenses = [{"category": "food", "amount": 200}, {"category": "transport", "amount": 150}, {"category": "food", "amount": 300}]
    result = total_spent(expenses)

    assert result == 650

def test_total_empty():

    expenses = []
    result = total_spent(expenses)

    assert result == 0

def test_total_one_expense():

    expenses = [{"category": "food", "amount": 75}]
    result = total_spent(expenses)

    assert result == 75

## Tests for spent_by_category ##

def test_spent_by_category_multiple_expense():

    expenses = [
        {"category":"food","amount":200},
        {"category":"transport","amount":400},
        {"category":"food","amount":1000}
    ]

    result = spent_by_category(expenses)
    assert result == {"food":1200,"transport":400}

def test_spent_by_category_empty():

    expenses = []

    result = spent_by_category(expenses)
    assert result == {}

def test_spent_by_category_one_category_summed():

    expenses = [
        {"category":"food","amount":100},
        {"category":"food","amount":400}
    ]

    result = spent_by_category(expenses)
    assert result == {"food":500}

def test_spent_by_category_one_category():

    expenses = [
        {"category":"food","amount":100},
    ]

    result = spent_by_category(expenses)
    assert result == {"food":100}

def test_top_category_multiple_summed_category():

    expenses = [
        {"category":"food","amount":200},
        {"category":"oil","amount":100},
        {"category":"food","amount":600}
    ]

    result = top_category(expenses)
    assert result == "food"

def test_top_category_empty():

    expenses = []

    result = top_category(expenses)
    assert result == None

def test_top_category_one_expense():

    expenses = [
        {"category":"oil","amount":100}
    ]

    result = top_category(expenses)
    assert result == "oil"

def test_top_category_tied_expense():

    expenses = [
        {"category":"oil","amount":100},
        {"category":"fruits","amount":100}
    ]

    result = top_category(expenses)
    assert result == "oil"

def test_top_category_multiple_small_one_big_expense():

    expenses = [
        {"category":"oil","amount":100},
        {"category":"oil","amount":100},
        {"category":"oil","amount":100},
        {"category":"vegetables","amount":100}
    ]

    result = top_category(expenses)
    assert result == "oil"

