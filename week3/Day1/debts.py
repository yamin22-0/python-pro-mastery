#TODO: PART A:
#TODO: Check for add_debt(debts,name,amount): Make it so it rejects an empty name,amount of 0 and below and if a customer exists add amount to him if no exist create a new user.
#TODO: PART B:
#TODO: Check for pay_debt if no name is entered, if they're not in debts dictionary and if amount to pay is 0 or less than 0 and if payment exceeds amount owed.

def add_debt(debts,name,amount):

    name = name.strip().lower()

    if not name:
        return False, "Please enter name."
    elif amount <= 0:
        return False, "Please enter valid amount."
    else:
        debts[name] = debts.get(name, 0) + amount
        return True, "debt added."

def total_owed(debts):

    owing = 0

    for debt in debts.values():
        owing += debt
    return owing

def pay_debt(debts,name,amount):

    name = name.strip().lower()

    if name not in debts:
        return False, "User doesn't exist."
    elif amount <= 0:
        return False, "Please enter valid amount."
    elif amount > debts[name]:
        return False, "Payment exeeds debt amount."
    else:
        debts[name] -= amount
        if debts[name] == 0:
            del debts[name]
        return True, "payment recorded."

