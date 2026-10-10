#TODO: Ask user for prices(1,2 and 3).
#TODO: Validate if prices are only float and a number above 0.
#TODO: Validate if discount is only for sub_total of 1000 going up.
#TODO: Calculate sub_total = sum([price_1,price_2,price_3]).
#TODO: Calculate discount_rate =10%(0.10) , discount_amount = sub_total * discount_rate
#         discounted_subtotal = sub_total - discount_amount.
#TODO: Calculate vat_amount = discounted_subtotal * vat_rate (0.16)
#TODO: Calculate final_total = discounted_subtotal + vat_amount.
#TODO: print(f"The items cost {sub_total} with a discount of {discount_amount} and a vat of {vat_amount} and final price is {final_total.")

def get_price():

    while True:
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Enter correct price.")
            continue
        if price <= 0:
            print("Price amount must be above 0.")
            continue
        return price

def apply_discount(total,percent):

    discount_amount = total * (percent / 100)
    discounted_total = total - discount_amount
    return discounted_total

def add_vat(amount):
    return amount * 1.16

def print_receipt(sub_total,discount_amount,vat_amount,final_total):
    print(f"The sub total is {sub_total:.2f} and the discount is {discount_amount:.2f}. The value added tax is {vat_amount:.2f} and the final amount to pay is {final_total:.2f}")

price_1 = get_price()
price_2 = get_price()
price_3 = get_price()

sub_total = price_1 + price_2 + price_3

if sub_total >= 1000:
    percent = 10
else:
    percent = 0

discounted_subtotal = apply_discount(sub_total,percent)
discount_amount = sub_total - discounted_subtotal

final_total = add_vat(discounted_subtotal)
vat_amount = final_total - discounted_subtotal

print_receipt(sub_total, discount_amount, vat_amount, final_total)


