# Inventory

## What it does ##
Keeps a shop's items with a quantity and a price. It can add an item, sell an item,
list items that are low in stock, and work out the total value of all the stock.

## Data model ##

-An item has: name, qty (quantity), price.
-The dictionary key is the cleaned lowercase name. The value is another dictionary.
**Example:**

  inventory = {
      "rice":  {"qty": 10, "price": 120},
      "beans": {"qty": 3,  "price": 90},
  }

## What each function takes and returns ##

**add_item(inventory, name, qty, price)**: returns (True/False, message).

**sell_item(inventory, name, qty)**: returns (True/False, message).

**low_stock(inventory, limit)**: returns a list of item names.

**total_value(inventory)**: returns a number.

## What can go wrong ##

`add_item(inventory,name,qty,price)`

**Empty inputs** - User may leave inventory input as empty. return False, "Enter an item please". 
**Duplicate Item** - User may try to add an item that already exists.
return False, "Item already exist."
**Negative Quantity** - The quantity is below 0, return False, "Enter valid quantity."
**Invalid price** - The price is 0 or less (negative or zero), return False "Enter valid price."

`sell_item(inventory, name, qty)`

**Missing Item** - The item does not exist in the inventory, return False, "Add Item first".

**Invalid Quantity** - to Sell: The quantity requested to sell is 0 or negative, return False, "Low quantity restock to start selling.".

**Insufficient Stock** The requested quantity is greater than what is currently available in stock, return False, "Please restock to continue this order".

`low_stock(inventory, limit)`

**Empty Inventory** If the dictionary is completely empty, it should safely return an empty list [] instead of throwing an error.

`total_value(inventory)`

**Empty Inventory** If the inventory has no items, it should return 0 instead of breaking.
