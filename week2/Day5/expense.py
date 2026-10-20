#TODO: Validate for add_expense(expenses,category,amount) if category is empty or amount is or less than 0. 


def add_expense(expenses,category,amount):

    category = category.strip().lower()

    if not category:
        return False, "Please enter category."
    elif amount <= 0:
        return False, "Please enter valid amount."
    else:
        expenses.append({"category":category,"amount":amount})
        return True, "Expense tracked succesfully"

def total_spent(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

