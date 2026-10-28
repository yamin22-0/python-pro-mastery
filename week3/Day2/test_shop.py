from shop import parse_amount,save_prices,load_prices
import pytest,json

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

def test_save_prices_and_load_prices(tmp_path):

    filename = tmp_path / "prices.json"
    prices = {"milk":60,"bread":80}
    save_prices(prices,filename)

    assert filename.exists()

    loaded = load_prices(filename)
    assert loaded == prices

def test_load_prices_missing_file(tmp_path):

    filename = tmp_path / "missing.json"
    loaded = load_prices(filename)
    assert loaded == {}

def test_load_prices_damaged_file(tmp_path):

    filename = tmp_path / "prices.json"
    filename.write_text("this file is damaged.")
    loaded = load_prices(filename)
    assert loaded == {}

def test_load_prices_empty_file(tmp_path):

    filename = tmp_path / "prices.json"
    filename.write_text(" ")
    loaded = load_prices(filename)
    assert loaded == {}


