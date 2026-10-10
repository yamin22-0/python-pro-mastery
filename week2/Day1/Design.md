## What system i'm building today ##

A shop reciept system where it asks user for 3 items , prints the subtotal(b4 subtracting discount, or adding VAT) then prints discount(only if sub_total is above or 1000), then prints the VAT , and then finally prints total.

## Information the system needs ##

**Inputs** `price` - price for the 3 items.`(price_1,price_2,price_3)`
**Processed info** `discount_amount`, `discount_rate`,`vat_amount`,`discounted_subtotal`,
**Outputs** `sub_total`, `vat_amount` ,`final_total`,`discount_amount`

## Rules ## 

1.`Price Validation` can only be numbers (float) and not less than 0. price > 0.
2.`Discount` is only for subtotal of 1000 and above.
3.First get sub_total `(sum(prices))`.
4.Second we get the `discount` discount_amount = sub_total * 0.10  (discounted_amount = sub_total - discount_amount).
5.Add `VAT`. (add_vat = discounted_amount * 1.16)
6.For printing the final reciept the eg `(1252.80)` , use `round()`

## What could go wrong ## 

**Empty types**
User may leave prices empty.

**Invalid Types**
User may enter price as 0 or (- number).
User may type (abc) 

## What each function should do ## 
1.The `get_price()` function - gets price_1,price_2 and price_3 **price = float(input("Enter price: ))**.
2.The `apply_discount(sub_total,percent)` - Calculates discount and subtracts it from subtotal.
3.The `add_vat(amount)` - adds the 16% VAT.
4.The `print_receipt(sub_total, discount_amount, vat_amount, final_total)` - neatly prints out all four formatted values using `:.2f` inside an f-string.
