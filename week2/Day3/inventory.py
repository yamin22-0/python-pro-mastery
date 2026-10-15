#TODO: Initialise the empty inventory. `inventory = {}`.
#TODO: PART A.
# TODO: Validate for add_items empty inventory name , a name that exists a quantity below 0 and price of 0 or below 0.
# TODO: Calculate total_value(invetory).
# TODO: PART B.
#TODO: Validate for sell_item if item exists,and if quantity is above 0,if trying to sell more than it's in stock.
#TODO: Output for low_stock(inventory,limit) - for stock that is at or below the limit.



def add_item(inventory,name,quantity,price):

    name = name.strip().lower()

    if not name :
        return False, "Enter an Item please."
    elif name in inventory:
        return False, "Item already exists."
    elif quantity < 0:
        return False, "Enter valid Quantity."
    elif price <= 0:
        return False, "Enter valid price."
    else:
        inventory[name] = {"qty":quantity, "price":price }
        return True, "Item added successfully"


def total_value(inventory):

    total = 0

    for name, item in inventory.items():
        total += item["qty"] * item["price"]

    return total

def sell_item(inventory,name,quantity):

    name = name.strip().lower()
    

    if not name:
        return False, "Enter item please."
    elif name not in inventory:
        return False, "Enter item that exists."
    elif quantity <= 0:
        return False, "Low quantity restock to start selling.."
    elif quantity > inventory[name]["qty"]:
        return False, "Please restock to continue this order."
    else:
        inventory[name]["qty"] -= quantity
        return True, "Item sold."

def low_stock(inventory,limit):

    low_items = []

    for name, item in inventory.items():
        if item["qty"] <= limit:
            low_items.append(name)

    return low_items

