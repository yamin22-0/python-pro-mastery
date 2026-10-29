from shop import parse_amount,save_prices,load_prices,set_price
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

def test_parse_amount_nan():

    with pytest.raises(ValueError, match="Price must be finite number."):
        parse_amount("nan")

def test_parse_amount_finite():

    with pytest.raises(ValueError, match="Price must be finite number."):
        parse_amount("inf")

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
    filename.write_text("")
    loaded = load_prices(filename)
    assert loaded == {}

def test_set_price_good():

    prices = {}
    result = set_price(prices,"milk",60.0)

    assert result[0] == True
    assert result[1] == "Price set successfully."
    assert prices["milk"] == 60.0

def test_set_price_replace():

    prices = {"milk":"60"}
    result = set_price(prices,"milk","70")

    assert result[0] == True
    assert prices["milk"] == 70.0

def test_set_price_bad_price():

    prices = {}
    result = set_price(prices,"sugar","abc")

    assert result[0] == False
    assert prices == {}

def test_set_price_zero_price():

    prices = {}
    result = set_price(prices,"sugar","0")

    assert result[0] == False
    assert prices == {}

def test_set_price_negative_price():

    prices = {}
    result = set_price(prices,"sugar","-100")

    assert result[0] == False
    assert prices == {}

def test_set_price_empty_name():

    prices = {}
    result = set_price(prices," ","200")

    assert result[0] == False
    assert prices == {}

def test_set_price_name_cleaning():

    prices = {}
    result = set_price(prices," HONEY ","250")

    assert result[0] == True
    assert " HONEY " not in prices
    assert "honey" in prices
    assert prices["honey"] == 250.0

