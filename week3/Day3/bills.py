from date_helper import parse_date
from datetime import date

def add_bill(bills,name,amount,due_text):

    name = name.strip().lower()

    if not name:
        return False, "Please enter name."
    elif name in bills:
        return False, "User already exists."
    elif amount <= 0:
        return False, "Please enter valid amount."

    try:
        parsed_date = parse_date(due_text)
    except ValueError as error:
        return False, str(error)

    bills[name] = {
        "amount":amount, "due":parsed_date.isoformat()
    }
    return True, "Bill added successfully."
