from expense import add_expense

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
