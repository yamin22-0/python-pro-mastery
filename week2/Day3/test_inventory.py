from inventory import add_item,total_value,sell_item


def test_add_item_good():
    inventory = {}
    name,qty,price = "sugar",20,200

    result = add_item(inventory,name,qty,price)
    assert result[0] == True
    assert result[1] == "Item added successfully"
    assert inventory[name]["qty"] == qty

def test_add_item_duplicate():
    inventory = {}
    add_item(inventory,"rice",10,120)

    result = add_item(inventory,"rice",10,120)
    
    assert result[0] == False
    assert inventory["rice"]["qty"] == 10

def test_add_item_empty_name():
    inventory = {}
    name,qty,price = " ",10,300
    result = add_item(inventory,name,qty,price)
    assert result[0] == False
    assert inventory == {}

def test_add_item_negative_qty():
    inventory = {}
    name,qty,price = "mango",-10,100
    result = add_item(inventory,name,qty,price)
    assert result[0] == False
    assert "mango" not in inventory


def test_add_item_zero_price():
    inventory = {}
    name,qty,price = "wheat",10,0
    result = add_item(inventory,name,qty,price)
    assert result[0] == False
    assert "wheat" not in inventory


def test_add_item_name_cleaning():
    inventory = {}
    name,qty,price = " RICE ",15,145
    result = add_item(inventory,name,qty,price)
    assert result[0] == True
    assert "rice" in inventory
    assert " RICE " not in inventory

def test_total_value_with_items():

    inventory = {"rice": {"qty": 10, "price": 120}, 
                 "beans": {"qty":3, "price": 90} }
    result = total_value(inventory)
    assert result == 1470

def test_total_value_without_items():

    inventory = {}
    result = total_value(inventory)
    assert result == 0

def test_sell_item_good():

    inventory = {"rice": {"qty": 10, "price": 120}}
    result = sell_item(inventory,"rice",4)
    assert result[0] == True
    assert inventory["rice"]["qty"] == 6

def test_sell_item_empty_name():

    inventory = {"sugar": {"qty": 15, "price": 200}}
    result = sell_item(inventory," ",5)
    assert result[0] == False
    assert inventory == {"sugar": {"qty": 15, "price": 200}}

def test_sell_item_non_existent_item():

    inventory = {"milk": {"qty":5, "price":400}}
    result = sell_item(inventory,"orange",2)

    assert result[0] == False
    assert "orange" not in inventory
    assert inventory["milk"]["qty"] == 5

def test_sell_item_negative_quantity():

    inventory = {"sorghum": {"qty":30,"price":155}}
    result = sell_item(inventory,"sorghum",-10)

    assert result[0] == False
    assert inventory["sorghum"]["qty"] == 30

def test_sell_item_zero_quantity():

    inventory = {"barley": {"qty":25,"price":200}}
    result = sell_item(inventory,"barley",0)

    assert result[0] == False
    assert inventory["barley"]["qty"] == 25

def test_sell_item_low_stock():

    inventory = {"wheatabix": {"qty":5,"price":500}}
    result = sell_item(inventory,"wheatabix",7)

    assert result[0] == False
    assert inventory["wheatabix"]["qty"] == 5

