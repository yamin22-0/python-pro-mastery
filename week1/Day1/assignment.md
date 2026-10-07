Day 1: Bill Splitter

The problem in plain English: a group eats at a restaurant. The program asks for the total bill, how many people shared it, and the tip percentage. It then prints the total with tip, and how much each person pays.

Example: bill 2000, 4 people, tip 10%. The total is 2200 and each person pays 550.

Do it in this order:

Write your design note in DESIGN.md, using the four questions above. It should take 5 minutes. Your "what can go wrong" list should have at least two things (hint: look at the airtime example).
Write the TODO comments for each step before you write any code.
Write the code under the comments.
Test it with the example above, and with 1 person.

New tools for today (tiny examples with different data):

python
price = float(input("Price: "))     
print(round(price / 3, 2))         
print(f"Total is {price}")    