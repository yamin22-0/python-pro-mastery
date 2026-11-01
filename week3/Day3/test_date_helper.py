from date_helper import parse_date,days_until
from bills import add_bill
import pytest
from datetime import date

def test_parse_date_good_and_cleaning():

    result1 = parse_date("2026-11-05")
    result2 = parse_date(" 2026-11-5 ")
    assert result1 == date(2026,11,5)
    assert result2 == date(2026,11,5)

def test_parse_date_empty_date():

    with pytest.raises(ValueError,match="Please enter a date."):
        parse_date("")

def test_parse_date_invalid_inputs():

    for invalid_texts in ["hello","05-11-2025","2026-13-10","2026-02-30"]:
        with pytest.raises(ValueError,match="valid"):
            parse_date(invalid_texts)

def test_parse_date_leap_year():

    result = parse_date("2024-02-29")
    assert result == date(2024,2,29)          


def test_parse_date_not_leap_year():

    with pytest.raises(ValueError, match="valid"):
        parse_date("2026-2-29")

def test_days_until_positive():

    assert days_until(date(2026,11,10),date(2026,11,4)) == 6

def test_days_until_equal():

    assert days_until(date(2026,10,31),date(2026,10,31)) == 0
    
def test_days_until_negative():

    assert days_until(date(2026,11,10),date(2026,11,15)) == -5

def test_add_bills_good():

    bills = {}
    name,amount,due_text = ("rent",30000,"2026-12-01")
    result = add_bill(bills,name,amount,due_text)

    assert result[0] == True
    assert result[1] == "Bill added successfully."
    assert bills["rent"] == {"amount":30000,"due":"2026-12-01"}

def test_add_bills_good_stripping_date():

    bills = {}
    name,amount,due_text = ("rent",30000," 2026-12-01 ")
    result = add_bill(bills,name,amount,due_text)

    assert result[0] == True
    assert result[1] == "Bill added successfully."
    assert bills["rent"] == {"amount":30000,"due":"2026-12-01"}

def test_add_bill_duplicate_name():

    bills = {"entertainment": {"amount":2000,"due":"2026-12-05"}}
    result = add_bill(bills,"entertainment",2000,"2026-12-05")

    assert result[0] == False
    assert bills["entertainment"] == {"amount":2000,"due":"2026-12-05"}

def test_add_bill_empty_name():

    bills = {}
    result = add_bill(bills,"",3000,"2026-11-29")

    assert result[0] == False
    assert bills == {}

def test_add_bill_zero_amount():

    bills = {}
    result = add_bill(bills,"detergents",0,"2026-11-29")

    assert result[0] == False
    assert bills == {}

def test_add_bill_bad_date():

    bills = {}
    result = add_bill(bills,"rent",3000,"hello")

    assert result[0] == False
    assert bills == {}

def test_add_bill_empty_name():

    bills = {}
    result = add_bill(bills,"",3000,"2026-11-29")

    assert result[0] == False
    assert bills == {}

def test_add_bill_cleaning_name():

    bills = {}
    result = add_bill(bills," WATER ",5000,"2026-12-05")

    assert result[0] == True
    assert result[1] == "Bill added successfully."
    assert "water" in bills
    assert " WATER " not in bills
    assert bills["water"] == {"amount":5000,"due":"2026-12-05"}

