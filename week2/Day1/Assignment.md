Week 2, Day 1: Shop Receipt

New idea: return. A function that only prints can’t hand its answer to the rest of the program. One that returns can. Here it is on different data:

python
def add_tax(price):
    return price * 1.10          # gives the answer back

def apply_coupon(price, off):
    return price - off

total = add_tax(100)             # 110.0
total = apply_coupon(total, 10)  # a function's answer can be passed to another function
print(total)                     # 100.0

The problem in plain English: a shop receipt, built from small functions. The program asks for 3 item prices, then prints the subtotal, the discount, the VAT, and the final total.

Write these four functions, each doing one job:

get_price(): asks for one price, checks it’s a number above 0 (asking again if not), and returns it.
apply_discount(total, percent): returns the total after taking off the percent.
add_vat(amount): returns the amount plus 16% VAT.
print_receipt(...): prints the lines. This is the only function that prints the results.

Rules:

Discount: 10% if the subtotal is 1000 or more, otherwise 0%.
The order is subtotal, then discount, then VAT on the discounted amount.
Round money to 2 decimal places when printing.

Example: prices 500, 400 and 300 give a subtotal of 1200, a discount of 10% (120), a discounted total of 1080, VAT of 172.80, and a final total of 1252.80.

Do it in this order:

Create a Week2/Day1 folder and write DESIGN.md with the four questions, plus one line per function saying what goes in and what comes out. Send it to me before you code.
Code one function at a time, and test each by itself, for example print(add_vat(100)), before using it in the program.
Test with the example, plus prices of abc, 0 and -5, and a subtotal of exactly 1000 (is the discount applied?).
DSA warm-up (30 minutes)

Write a function find_largest(numbers) that takes a list and returns the biggest number, using a for loop and without max().

Hint: keep a variable called largest, and update it whenever you meet a bigger number. This is the same shape as your pass counter, only it remembers a number instead of counting.

Test with: [3, 9, 2], [-5, -1, -8] and [7]. Then write one sentence in your log about why you start largest at the first item and not at 0. The second test shows why.