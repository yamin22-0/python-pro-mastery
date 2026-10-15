from inventory import add_item


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
    name,qty,price = "RICE",15,145
    result = add_item(inventory,name,qty,price)
    assert result[0] == True
    assert "rice" in inventory
    assert " RICE " not in inventory