#TODO: PART A:
#TODO: Check for add_debt(debts,name,amount): Make it so it rejects an empty name,amount of 0 and below and if a customer exists add amount to him if no exist create a new user.

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

