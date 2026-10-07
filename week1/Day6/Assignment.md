Day 6, twist on the contact book

No new tools today. You use what you already know on your finished program. Copy your Day 5 file into a Day6 folder first, so Day 5 stays untouched.

Step 1: Update DESIGN.md (about 15 minutes, send it to me before you code). Add two new rules, each with a worked example:

Option "Update phone number":
The user types a name, which is cleaned the usual way.
If the name exists, they type a new phone number, checked by the same 10-digit rule as Add.
If the name isn't in the book, print a message.
Example: amina has 0711111111. Update amina to 0722222222, then find her and see the new number.
Find with part of a name:
Typing binyamin finds binyamin ahmed. If several names match, print all of them. If none match, print "Contact not found".
Example: the book has binyamin ahmed and binyamin ali. Searching binyamin prints both. Searching ahm prints only the first.

Also decide where the new menu item goes (I'd make Update option 4, and move Show all and Quit down), and write the new menu in the note. Add the new things that can go wrong: an empty search, a new phone number that's invalid, and updating a name that doesn't exist.

Step 2: Write the TODO comments for the two new features.

Step 3: Code Update first. It's the easier of the two, and it looks like your Delete and Add blocks combined. After the name is found, ask for the phone, check it, and store it with contact_list[name] = new_phone, which replaces the old value. Run and test it before moving on.

Step 4: Then code the partial Find. Two hints:

in works on text: "bin" in "binyamin" is True.
A for name in contact_list: loop gives you each name. Keep a counter or a flag so you know if anything matched, and print "Contact not found" only if nothing did.

Step 5: Test.

both worked examples
an update with a 9-digit number: rejected, and the old number stays
an update of a name that doesn't exist
a search that matches two names, one name, and none
an empty search (think about what "" in "binyamin" does, and decide how you want to handle it, then write it in your design)