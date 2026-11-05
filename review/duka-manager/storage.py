import json

#TODO: new_data
#TODO: save_data(data,filename)
#TODO: load_data(filename)

def new_data():

    return {
            "products": {}, 
            "sales": [], 
            "debts": {}, 
            "bills": {}
            }

def save_data(data,filename):

    with open(filename, "w") as f:
        json.dump(data,f)

def load_data(filename):

    try:
        with open(filename, "r") as f:
            data = json.load(f)

        if type(data) is not dict:
            return new_data()

        if "products" not in data:
            data["products"] = {}
        if "sales" not in data:
            data["sales"] = []
        if "debts" not in data:
            data["debts"] = {}
        if "bills" not in data:
            data["bills"] = {}

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return new_data()

