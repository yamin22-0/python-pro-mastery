from datetime import datetime

class User:
    def __init__(self, name, phone_number, transactions=None, balance=0):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.transactions = [] if transactions is None else transactions

    @staticmethod
    def normalise_phone(raw):
        raw = raw.strip()
        raw = raw.replace(" ", "").replace("-", "")

        if raw.startswith("+254"):
            raw = "0" + raw[4:]
        elif raw.startswith("254"):
            raw = "0" + raw[3:]

        if len(raw) != 10 or not raw.isdigit() or not raw.startswith(("07", "01")):
            return None

        return raw


def find_user(users, raw_phone):
    phone = User.normalise_phone(raw_phone)

    if phone is None:
        return None

    if phone in users:
        return users[phone]

    return None



def deposit(users, raw_phone, amount):
    user = find_user(users, raw_phone)

    if user is None:
        return (False, "Number is not registered.")
    try:
        amount = float(amount)
    except ValueError:
        return (False, "Amount must be a number")

    if amount <= 0:
        return (False, "Enter a valid amount")

    user.balance += amount

    user.transactions.append({
        "type": "deposit",
        "amount": amount,
        "fee": 0,
        "other_party": None,
        "balance_after": user.balance,
        "time": datetime.now()
    })

    return (True, "Deposit Successful")

def withdraw(users,raw_phone,amount):
    user = find_user(users,raw_phone)

    if user is None:
        return (False , "Number not registered.")

    try:
        amount = float(amount)
    except ValueError:
        return (False, "Amount must be a number.")

    if amount <= 0:
        return (False, "Amount can't be negative.")

    fee = 10
    total_deduction = amount + fee

    if user.balance < total_deduction:
        return (False, "Insufficient funds for the operation to continue.")

    user.balance -= total_deduction

    user.transactions.append({
        "type" : "withdraw",
        "amount" : amount,
        "fee" : fee,
        "balance_after" : user.balance,
        "other_party": None,
        "time" : datetime.now()
    })

    return (True, "Withdrawal succesful.")


def register_number(users, name, raw_phone):
    phone = User.normalise_phone(raw_phone)
    if phone is None:
        return (False, "Invalid phone number")

    if phone in users:
        return (False, "Number already registered.") 

    users[phone] = User(name, phone)

    return (True, "Registration Succesful")


# --- Tests ---
users = {}

print(register_number(users, "Amina", "0711111111"))
print(register_number(users, "Amina", "+254711111111"))
print(register_number(users, "Test", "07123"))
print(len(users))

print(User.normalise_phone("0712345678"))
print(User.normalise_phone("+254712345678"))
print(User.normalise_phone("254712345678")) 
print(User.normalise_phone("071 234 5678"))
print(User.normalise_phone("07123"))
print(User.normalise_phone("abc"))
print(User.normalise_phone("0812345678"))
print(User.normalise_phone("0712345"))

print(deposit(users, "0711111111", 500))       
print(deposit(users, "+254711111111", "250"))  
print(deposit(users, "0799999999", 100))       
print(deposit(users, "0711111111", 0))         
print(deposit(users, "0711111111", -50))       
print(deposit(users, "0711111111", "abc"))     
print(users["0711111111"].balance)             
print(len(users["0711111111"].transactions))

register_number(users, "Amina", "0711111111")
register_number(users, "Brian", "0722222222")
deposit(users, "0711111111", 750)
deposit(users, "0722222222", 750)

print(withdraw(users, "0711111111", 740))     
print(users["0711111111"].balance)            
print(withdraw(users, "0711111111", 1))        
print(withdraw(users, "0722222222", 741))      
print(users["0722222222"].balance)             
print(withdraw(users, "0722222222", 740))      
print(withdraw(users, "0799999999", 100))      
print(withdraw(users, "0722222222", "abc"))    