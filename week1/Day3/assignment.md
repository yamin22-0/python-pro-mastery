Day 3: Shopping List

New tools: lists, .append(), .remove(), len() and in. Here they are on different data:

python

tasks = []                      # an empty list
tasks.append("wash clothes")    # adds to the end
tasks.append("cook")
print(tasks)                    # ['wash clothes', 'cook']
print(len(tasks))               # 2

if "cook" in tasks:             # in checks if something is in the list
    tasks.remove("cook")        # removes it
print(tasks)                    # ['wash clothes']

tasks.remove("sleep") when "sleep" isn't in the list crashes, which is why the in check comes first.

The problem in plain English: the program asks for exactly 3 items to buy, one at a time, and puts them in a list. It then prints the list and how many items there are. It asks which item to remove, removes it, and prints the list and count again.

Rules:

Items are cleaned with .strip().lower(), so "Milk" and " milk " are the same.
An empty item is rejected, and so is an item that's already on the list. In both cases the program says why and doesn't add it.
If the item to remove isn't on the list, print a message and don't crash.

Example: add milk, bread, sugar, then remove bread. You get ['milk', 'sugar'] and 2 items.

Do it in this order:

Create a Day3 folder and write DESIGN.md: the four questions, in your own words. Include what the list holds and every rule above.
Send me the design note before you code.
Write the TODO comments, code one at a time, and run after each.
Test with the example, plus:
a duplicate item
an empty item
removing something that isn't there

Then write 3 or 4 lines in LOG.md, in your own words, and commit with a message like week1-day3: shopping list.
this is todays assignment first start with design.md then bring u review find problems and give me a small hint i re-fix then make TODO: then start coding.