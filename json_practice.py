import json

students = {"binyamin":3359,"halima":2232}

with open("students.json", "w") as f:
    json.dump(students,f)
print("saved")

with open("prices.json") as f:
    loaded = json.load(f)

print(loaded)

import os

if os.path.exists("nothing.json"):
    with open("nothing.json") as f:
        loaded = json.load(f)
else:
    loaded = {}

print(loaded)

def save_prices(prices, filename):
    with open(filename, "w") as f:
        json.dump(prices, f)

def load_prices(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename) as f:
        return json.load(f)

save_prices({"tea": 30}, "test.json")
print(load_prices("test.json"))       # {'tea': 30}
print(load_prices("missing.json"))    # {}
