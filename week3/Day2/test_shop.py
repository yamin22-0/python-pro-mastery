from shop import parse_amount
import pytest

# Tests for parse_amount(text) 

def test_parse_amount_good():

    result = parse_amount("500")
    assert result == 500.0

def test_parse_amount_good_decimal():

    result = parse_amount(" 250.5 ")
    assert result == 250.5

def test_parse_amount_word():

    with pytest.raises(ValueError, match="Please enter price"):
        parse_amount("abc")
def test_parse_amount_zero():

    with pytest.raises(ValueError, match="positive"):
        parse_amount("0")

def test_parse_amount_negative():

    with pytest.raises(ValueError, match="positive"):
        parse_amount("-70")

def test_parse_amount_empty():

    with pytest.raises(ValueError, match="Please enter price"):
        parse_amount(" ")
