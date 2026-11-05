from validators import clean_name, parse_amount, parse_date, parse_quantity
import pytest
from datetime import date

def test_parse_amount_good():
    result = parse_amount("500")
    assert result == 500.0

def test_parse_amount_decimal():
    result = parse_amount("250.5")
    assert result == 250.5

def test_parse_amount_nan():
    with pytest.raises(ValueError, match="Please enter valid finite price"):
        parse_amount("nan")

def test_parse_amount_inf():
    with pytest.raises(ValueError, match="Please enter valid finite price"):
        parse_amount("inf")

def test_parse_amount_abc():
    with pytest.raises(ValueError,match="Please enter price."):
        parse_amount("abc")

def test_parse_amount_zero():
    with pytest.raises(ValueError,match="Please enter a valid price."):
        parse_amount("0")

def test_parse_amount_negative():
    with pytest.raises(ValueError,match="Please enter a valid price."):
        parse_amount("-5")

def test_parse_amount_empty():
    with pytest.raises(ValueError,match="Please enter price."):
        parse_amount("")

def test_parse_quantity_good():
    result = parse_quantity("3")
    assert result == 3
    assert isinstance(result, int)

def test_parse_quantity_good_cleaning():
    result = parse_quantity(" 3 ")
    assert result == 3
    assert isinstance(result, int)

def test_parse_quantity_decimal():
    with pytest.raises(ValueError, match="Please enter valid quantity amount."):
        parse_quantity("2.5")

def test_parse_quantity_abc():
    with pytest.raises(ValueError, match="Please enter valid quantity amount."):
        parse_quantity("abc")

def test_parse_quantity_empty():
    with pytest.raises(ValueError, match="Please enter valid quantity amount."):
        parse_quantity("")

def test_parse_quantity_zero():
    with pytest.raises(ValueError, match="Please enter quantity above 0."):
        parse_quantity("0")

def test_parse_quantity_negative():
    with pytest.raises(ValueError, match="Please enter quantity above 0."):
        parse_quantity("-1")

def test_parse_date_good():
    assert parse_date("2026-11-05") == date(2026,11,5)
    assert parse_date("2024-02-29") == date(2024,2,29)
    assert parse_date(" 2026-11-05 ") == date(2026,11,5)

def test_parse_date_bad():
    bad_input =["05-11-2026","2026-13-01","2026-02-29",""]

    for bad in bad_input:
        with pytest.raises(ValueError, match="Please enter correct date format."):
            parse_date(bad)

def test_clean_name_good():
    assert clean_name(" MILK ") == "milk"
