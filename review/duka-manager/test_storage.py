from storage import new_data,save_data,load_data
import json

def test_new_data_empty(tmp_path):
    data = new_data()

    assert data == {
         "products": {}, 
        "sales": [], 
        "debts": {}, 
        "bills": {}
    }

def test_double_instances():

    data1 = new_data()
    data2 = new_data()
    data1["milk"] = {"qty":10,"price":60.0}

    assert "milk" not in data2

def test_save_and_load_data(tmp_path):

    filename = tmp_path / "duka.json"
    data = {
        "products" : {"sugar" : {"qty":30,"price":600}},
        "sales": [],
        "debts": {},
        "bills": {}
    }

    save_data(data,filename)
    assert filename.exists()

    loaded_data = load_data(filename)
    assert loaded_data == data

def test_load_data_missing(tmp_path):

    filename = tmp_path / "notexixst.json"
    data = load_data(filename)

    assert data == new_data()

def test_load_data_not_json(tmp_path):

    filename = tmp_path / "duka.json.json"
    filename.write_text("This is not json.")
    data = load_data(filename)
    assert data == new_data()

def test_load_data_empty_file(tmp_path):

    filename = tmp_path / "empty.json"
    filename.write_text("")
    data = load_data(filename)
    assert data == new_data()

def test_load_data_file_containing_numbers(tmp_path):

    filename = tmp_path / "duka.json.json"
    filename.write_text("[1,2]")
    data = load_data(filename)
    assert data == new_data()

def test_save_data_and_load_file_containing_products(tmp_path):

    filename = tmp_path / "products.json"
    filename.write_text('{"products": {"milk": {"qty": 1, "price": 5.0 }}}')
    data = load_data(filename)
    
    assert data["products"] == {"milk": {"qty": 1, "price": 5.0 }}
    assert data["sales"] == []
    assert data["debts"] == {}
    assert data["bills"] == {}
