Day 2: Matatu Fare Calculator

New tools: elif (more than two choices) and .lower() (makes text lowercase). Here is each on different data:

python
size = input("Size (small/medium/large): ").strip().lower()

if size == "small":
    price = 50
elif size == "medium":
    price = 80
elif size == "large":
    price = 120
else:
    print("Unknown size.")
    exit()

print(price)

.lower() makes "LARGE", "Large" and " large " all work the same (.strip() removes the extra spaces). Python checks the choices from top to bottom and stops at the first match, and else catches everything that matched nothing.

The problem in plain English: the program asks where the passenger is going, how many passengers there are, and whether it's peak time. It then prints the fare per person and the total.

Fares (made up):

Westlands: 50
Rongai: 80
Thika: 100
Kitengela: 120

Rules:

Peak time (the user answers yes or no) adds 30 to each person's fare.
The user may type the destination in any capital letters, with extra spaces.
An unknown destination prints a message and stops.

Examples:

Thika, 3 passengers, peak yes: each pays 130, total 390.
Thika, 3 passengers, peak no: each pays 100, total 300.

Do it in this order:

Create a Day2 folder and write DESIGN.md with the four questions, in your own words. For "what can go wrong", think about the destination, the passenger count, and the yes/no answer. Send me the design note before you write code.
Write the TODO comments.
Code one TODO at a time, and run after each one.
Test with both examples, plus these:
a destination typed as THIKA
an unknown town
abc as the passenger count
0 passengers

Then write 3 or 4 lines in LOG.md, in your own words, and commit with a message like week1-day2: matatu fare calculator.