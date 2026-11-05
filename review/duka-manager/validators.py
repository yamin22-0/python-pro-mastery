import math
from datetime import datetime

#TODO: Clean name.
#TODO: parse_amount.
#TODO: parse_date
#TODO: parse_quantity.

def clean_name(name):

    return name.strip().lower()

def parse_amount(text):

    try:
        price = float(text)
    except ValueError:
        raise ValueError("Please enter price.")

    if not math.isfinite(price):
        raise ValueError("Please enter valid finite price")

    if price <= 0:
        raise ValueError("Please enter a valid price.")

    return price

def parse_date(text):

    text = text.strip()

    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Please enter correct date format.")

    
def parse_quantity(text):

    try:
        quantity = int(text)
    except ValueError:
        raise ValueError("Please enter valid quantity amount.")

    if quantity <= 0:
        raise ValueError("Please enter quantity above 0.")

    return quantity
