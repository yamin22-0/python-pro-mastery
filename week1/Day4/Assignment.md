Day 4: Class Marks and Average

New tools: for loops and sum(). Here they are on different data:

python
prices = [120, 80, 200]

total = 0
for p in prices:            # p is each item in turn: 120, then 80, then 200
    total = total + p
print(total)                # 400
print(sum(prices))          # 400: sum() does the same thing in one step

count = 0
for p in prices:
    if p > 100:             # an if inside a for: check each item
        count += 1
print(count)                # 2 items are above 100

for i in range(3):          # range(3) makes 0, 1, 2: runs exactly 3 times
    print(i)

The problem in plain English: the program asks for the marks of 5 students, one at a time, and keeps them in a list. It then prints the total, the average (to 2 decimal places), the highest mark, the lowest mark, and how many students passed.

Rules:

A mark must be a number from 0 to 100. A word, or a number outside that range, is rejected with a message, and the program asks for that student's mark again.
A pass is 50 or more.
Use max() and min() for the highest and lowest. They work on a list, like sum().

Example: marks 70, 45, 88, 50, 62 give a total of 315, an average of 63.0, a highest of 88, a lowest of 45, and 4 passed.

Do it in this order:

Create a Day4 folder and write DESIGN.md with the four questions, in your own words. Include a worked example like the one above. Send me the design note before you code.
Write your TODO comments, then code one at a time, running after each.
Test with the example, plus a mark of 101, a mark of abc, and a mark of exactly 50 (it should count as a pass).