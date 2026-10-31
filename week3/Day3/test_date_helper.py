from date_helper import parse_date,days_until
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

