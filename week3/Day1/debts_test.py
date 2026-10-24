from debts import add_debt

## Tests for add_debt ##

def test_add_debt_good():

    debts = {}
    name,amount = "binka",500

    result = add_debt(debts,name,amount)
    assert result[0] == True
    assert result[1] == "debt added."
    assert debts[name] == 500

def test_add_debt_to_existing():

    debts = {"halima":500}
    result = add_debt(debts,"halima",500)

    assert result[0] == True
    assert debts["halima"] == 1000

def test_add_debt_empty_name():

    debts = {}
    result = add_debt(debts," ",200)

    assert result[0] == False
    assert debts == {}

def test_add_debt_amount_zero():

    debts = {}
    result = add_debt(debts,"zeo",0)

    assert result[0] == False
    assert debts == {}

def test_add_debt_negative_amount():

    debts = {}
    result = add_debt(debts,"zeke",-1)

    assert result[0] == False
    assert debts == {}

def test_add_debt_cleaning_name():

    debts = {}
    result = add_debt(debts," ALI ",250)

    assert result[0] == True
    assert result[1] == "debt added."
    assert "ali" in debts
    assert " ALI " not in debts
    assert debts["ali"] == 250
