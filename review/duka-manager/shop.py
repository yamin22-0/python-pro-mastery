from validators import clean_name,parse_date

def add_product(data,name,qty,price):
    name = clean_name(name)

    if not name:
        return False, "Please enter name."
    elif name in data["products"]:
        return False, "Product exists."
    elif qty < 0:
        return False, "Enter valid quantity."
    elif price <= 0:
        return False, "Enter valid price."
    else:
        data["products"][name] = {"qty":qty,"price":price}
        return True, "Product added successfully."

def restock(data,name,qty):

    name = clean_name(name)
    if name not in data["products"]:
        return False, "Product not found."
    elif qty <= 0:
        return False, "Please enter valid quantity."
    else:
        data["products"][name]["qty"] += qty
        return True, "Product restocked successfully."

def set_price(data,name,price):

    name = clean_name(name)
    if name not in data["products"]:
        return False, "Product not found."
    elif price <= 0:
        return False, "Enter correct price."
    else:
        data["products"][name]["price"] = price
        return True, "Price set successfully."

def find_products(data,name):

    search_name = clean_name(name)
    if not search_name:
        return []
    found = []

    for product_name in data["products"]:
        cleaned_name = clean_name(product_name)
        if search_name in cleaned_name:
            found.append(product_name)
    return found

def sell(data,name,qty,date_text,customer):

    name = clean_name(name)
    customer = clean_name(customer)

    if name not in data["products"]:
        return False, "Product not found."
    elif qty <= 0:
        return False, "Enter valid quantity"
    elif qty > data["products"][name]["qty"]:
        return False, "Invalid products count."

    try:
        parsed_date = parse_date(date_text)
    except ValueError as error:
        return False, str(error)

    price = data["products"][name]["price"]
    total = price * qty

    data["products"][name]["qty"] -= qty

    sales = {
        "product":name,
        "price":price,
        "quantity":qty,
        "date":parsed_date.isoformat(),
        "total":total,
        "customer":customer
    }

    data["sales"].append(sales)

    if customer:
        data["debts"][customer] = round(data["debts"].get(customer, 0.0) + total, 2)

    return True, "Product sold successfully."
