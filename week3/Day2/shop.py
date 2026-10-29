import json,math

#TODO: PART A
#TODO: Validate for parse_amount(text) if the input is empty,if input is a number and if it's 0 or less than 0.

def parse_amount(text):

    try:
        price = float(text)
    except ValueError:
        raise ValueError("Please enter price.")

    if not math.isfinite(price):
        raise ValueError("Price must be finite number.")


    if price <= 0:
        raise ValueError("Please enter a positive price.")
    return price

def save_prices(prices,filename):

    with open(filename, "w") as f:
        json.dump(prices,f)
    
def load_prices(filename):

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
 
def set_price(prices,name,text):

    name = name.strip().lower()

    if not name:
        return False, "Please enter a name."

    try:
        price = parse_amount(text)
    except ValueError as error:
        return False, str(error)

    prices[name] = price
    return True, "Price set successfully."
