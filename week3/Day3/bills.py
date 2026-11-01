from date_helper import parse_date,days_until
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

def overdue_bills(bills,today):

    result = []
    for name, bill in bills.items():
        due = parse_date(bill["due"])

        if days_until(due,today) < 0:
            result.append(name)
    return result

def due_soon(bills,today,days):

    result = []
    for name,bill in bills.items():
        soon = parse_date(bill["due"])

        if -100 <= days_until(soon,today) <= days:
            result.append(name)
    return result
