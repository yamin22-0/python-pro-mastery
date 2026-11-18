from shop import add_product,restock,set_price,find_products,sell
from storage import new_data

def test_add_product_good_product():
    data = new_data()
    result = add_product(data,"milk",20,60.0)
    assert result[0] == True
    assert result[1] == "Product added successfully."
    assert data["products"]["milk"] == {"qty":20,"price":60.0}

def test_add_product_name_cleaning():
    data = new_data()
    result = add_product(data," MILK ",20,60.0)
    assert result[0] == True
    assert result[1] == "Product added successfully."
    assert " MILK " not in data["products"]
    assert "milk" in data["products"]

def test_add_product_duplicate():
    data = new_data()
    add_product(data,"honey",5,500.0)
    result = add_product(data,"honey",2,400.0)
    assert result[0] is False
    assert data["products"]["honey"] == {"qty":5,"price":500.0}

def test_add_product_empty_name():
    data = new_data()
    result = add_product(data,"",3,350.0)
    assert result[0] == False
    assert data == new_data()

def test_add_product_negative_quantity():
    data = new_data()
    result = add_product(data,"bread",-2,60.0)
    assert result[0] == False
    assert data == new_data()

def test_add_product_zero_quantity():
    data = new_data()
    result = add_product(data,"mangoes",0,50.0)
    assert result[0] == True
    assert data["products"]["mangoes"] == {"qty":0,"price":50.0}

def test_add_product_zero_price():
    data = new_data()
    result = add_product(data,"bread",2,0)
    assert result[0] == False
    assert data == new_data()

def test_add_product_negative_price():
    data = new_data()
    result = add_product(data,"bread",2,-60)
    assert result[0] == False
    assert data == new_data()

def test_restock_good():
    data = new_data()
    add_product(data,"milk",20,60.0)
    result = restock(data,"milk",5)
    assert result[0] == True
    assert result[1] == "Product restocked successfully."
    assert data["products"]["milk"]["qty"] == 25

def test_restock_missing_product():
    data = new_data()
    add_product(data,"honey",2,200.0)
    result = restock(data,"bread",10)
    assert result[0] == False
    assert data["products"]["honey"] == {"qty":2,"price":200.0}

def test_restock_cleaning_name():
    data = new_data()
    add_product(data,"flour",10,75.0)
    result = restock(data," FLOUR ",5)
    assert result[0] == True
    assert "flour" in data["products"]
    assert " FLOUR " not in data["products"]
    assert data["products"]["flour"]["qty"] == 15

def test_restock_zero_quantity():
    data = new_data()
    add_product(data,"wheat",20,80.0)
    result = restock(data,"wheat",0)
    assert result[0] == False
    assert data["products"]["wheat"]["qty"] == 20

def test_restock_negative_quantity():
    data = new_data()
    add_product(data,"barley",20,80.0)
    result = restock(data,"barley",-10)
    assert result[0] == False
    assert data["products"]["barley"]["qty"] == 20

def test_restock_smallest_valid():
    data = new_data()
    add_product(data,"salt",10,30.0)
    result = restock(data,"salt",1)
    assert result[0] == True
    assert data["products"]["salt"]["qty"] == 11

def test_set_price_good():
    data = new_data()
    add_product(data,"mangoes",5,40.0)
    result = set_price(data,"mangoes",35.0)
    assert result[0] == True
    assert result[1] == "Price set successfully."
    assert data["products"]["mangoes"]["price"] == 35.0

def test_set_price_name_cleaning():
    data = new_data()
    add_product(data,"brush",11,30.0)
    result = set_price(data," BRUSH ",20.0)
    assert result[0] == True
    assert result[1] == "Price set successfully."
    assert "brush" in data["products"]
    assert " BRUSH " not in data["products"]
    assert data["products"]["brush"]["price"] == 20

def test_set_price_missing_product():
    data = new_data()
    add_product(data,"toothpaste",15,100.0)
    result = set_price(data,"colgate",90.0)
    assert result[0] == False
    assert data["products"]["toothpaste"]["price"] == 100.0

def test_set_price_zero_price():
    data = new_data()
    add_product(data,"orange",30,15.0)
    result = set_price(data,"orange",0)
    assert result[0] == False
    assert data["products"]["orange"]["price"] == 15.0

def test_set_price_negative_price():
    data = new_data()
    add_product(data,"orange",30,15.0)
    result = set_price(data,"orange",-12.0)
    assert result[0] == False
    assert data["products"]["orange"]["price"] == 15.0

def test_find_products_expected_same():
    data = new_data()
    add_product(data,"milk",5,60.0)
    add_product(data,"millet",15,120.0)
    add_product(data,"bread",9,80.0)
    result = find_products(data,"mil")
    assert result == ["milk", "millet"]

def test_find_products_capital():

    data = new_data()
    add_product(data,"milk",5,60.0)
    add_product(data,"millet",15,120.0)
    result = find_products(data,"MIL")
    assert result == ["milk", "millet"]

def test_find_products_full_name():
    data = new_data()
    add_product(data, "bread", 10, 50.0)
    
    result = find_products(data, "bread")
    assert result == ["bread"]

def test_find_products_no_match():
    data = new_data()
    add_product(data, "milk", 10, 60.0)
    
    result = find_products(data, "xyz")
    assert result == []

def test_find_products_empty_text():
    data = new_data()
    add_product(data, "milk", 10, 60.0)
    
    result = find_products(data, "")
    assert result == []

def test_find_products_spaces_only():
    data = new_data()
    add_product(data, "milk", 10, 60.0)
    
    result = find_products(data, "   ")
    assert result == []

def test_find_products_empty_inventory():
    data = new_data()
    result = find_products(data, "milk")
    assert result == []

def test_sell_credit_sale():
    data = new_data()
    add_product(data, "milk", 20, 60.0)
    
    result = sell(data, "milk", 2, "2026-11-01", "amina")
    
    assert result[0] is True
    assert data["products"]["milk"]["qty"] == 18
    assert data["debts"] == {"amina": 120.0}

def test_sell_cash_sale():
    data = new_data()
    add_product(data, "bread", 10, 50.0)
    
    result = sell(data, "bread", 2, "2026-11-01", "")
    
    assert result[0] is True
    assert data["products"]["bread"]["qty"] == 8
    assert data["sales"][-1]["customer"] == ""
    assert data["debts"] == {}

def test_sell_repeated_credit_sale():
    data = new_data()
    add_product(data, "sugar", 15, 100.0)
    
    sell(data, "sugar", 1, "2026-11-01", "amina")
    result = sell(data, "sugar", 2, "2026-11-02", "amina")
    
    assert result[0] is True
    assert data["debts"]["amina"] == 300.0  # 100 + 200

def test_sell_cleaning_customer_name():
    data = new_data()
    add_product(data, "tea", 10, 40.0)
    
    sell(data, "tea", 1, "2026-11-01", "  AMINA  ")
    
    assert "amina" in data["debts"]
    assert data["debts"]["amina"] == 40.0

def test_sell_exact_stock():
    data = new_data()
    add_product(data, "milk", 5, 60.0)
    
    result = sell(data, "milk", 5, "2026-11-01", "")
    
    assert result[0] is True
    assert data["products"]["milk"]["qty"] == 0

def test_sell_stock_plus_one():
    data = new_data()
    add_product(data, "milk", 5, 60.0)
    
    result = sell(data, "milk", 6, "2026-11-01", "")
    
    assert result[0] is False
    assert data["products"]["milk"]["qty"] == 5  # Unchanged

def test_sell_zero_quantity():
    data = new_data()
    add_product(data, "milk", 5, 60.0)
    
    result = sell(data, "milk", 0, "2026-11-01", "")
    
    assert result[0] is False

def test_sell_missing_product():
    data = new_data()
    result = sell(data, "butter", 2, "2026-11-01", "")
    assert result[0] is False

def test_sell_bad_date():
    data = new_data()
    add_product(data, "milk", 5, 60.0)
    
    result = sell(data, "milk", 2, "not-a-date", "")
    
    assert result[0] is False
