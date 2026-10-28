#TODO: PART A
#TODO: Validate for parse_amount(text) if the input is empty,if input is a number and if it's 0 or less than 0.

def parse_amount(text):

    try:
        price = float(text)
    except ValueError:
        raise ValueError("Please enter price.")


    if price <= 0:
        raise ValueError("Please enter a positive price.")
    return price



