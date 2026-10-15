#TODO: Initialise the empty inventory. `inventory = {}`.
#TODO: PART A.
# TODO: Validate for add_items empty inventory name , a name that exists a quantity below 0 and price of 0 or below 0.
# TODO: Calculate total_value(invetory).
# TODO: PART B.
#TODO: Validate for sell_item if item exists,and if quantity is above 0,if trying to sell more than it's in stock.
#TODO: Output for low_stock(inventory,limit) - for stock that is at or below the limit.


inventory = {}

def add_item(inventory,name,quantity,price):

    name = name.strip().lower()

    if not name :
        return False, "Item already exists."
    elif name in inventory:
        return False, "Enter an item please."
    elif quantity < 0:
        return False, "Enter valid Quantity."
    elif price <= 0:
        return False, "Enter valid price."
    else:
        inventory[name] = {"qty":quantity, "price":price }
        return True, "Item added successfully"



    

