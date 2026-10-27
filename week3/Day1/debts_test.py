from debts import add_debt,total_owed,pay_debt,save_debts,load_debts
import json

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

## Tests for total_owed ##

def test_total_owed_good():

    debts = {"binka":700,"hamza":1000}
    result = total_owed(debts)
    assert result == 1700

def test_total_owed_zero_debts():

    debts = {}
    result = total_owed(debts)
    assert result == 0

## Tests for pay_debts ##

def test_pay_debt_good():
    debts = {"amish": 800}
    result = pay_debt(debts, "amish", 200)

    assert result[0] == True
    assert result[1] == "payment recorded."
    assert debts["amish"] == 600

def test_pay_debt_boundary():

    debts = {"imran":500}
    result = pay_debt(debts,"imran",500)

    assert result[0] == True
    assert "imran" not in debts

def test_pay_debt_over_pay():

    debts = {"ahmed":400}
    result = pay_debt(debts,"ahmed",401)

    assert result[0] == False
    assert debts["ahmed"] == 400

def test_test_pay_debt_non_existant_user():

    debts = {"halima":230}
    result = pay_debt(debts,"hali",230)

    assert result[0] == False
    assert "hali" not in debts

def test_pay_debt_amount_zero():

    debts = {"moha":1000}
    result = pay_debt(debts,"moha",0)

    assert result[0] == False
    assert debts == {"moha":1000}

def test_pay_debt_name_cleaning():

    debts = {"amish":350}
    result = pay_debt(debts," AMISH ",150)

    assert result[0] == True
    assert debts["amish"] == 200

def test_save_debts_and_loaded(tmp_path):

    filename = tmp_path / "debts.json"
    debts = {"binka":200,"halima":500}
    save_debts(debts,filename)

    assert filename.exists

    loaded = load_debts(filename)
    assert loaded == debts

def test_load_debts(tmp_path):

    filename = tmp_path / "nothing.json"
    assert load_debts(filename) == {}

def test_save_debt_load_empty(tmp_path):

    filename = tmp_path / "debts.json"
    debts = {}
    save_debts(debts,filename)
    assert load_debts(filename) == {} 


