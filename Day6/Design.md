## What the system does ##

Today i'm building a contact book, This is a system that prompts user for name and then their phone number and stores in a dictionary.The prompt keeps asking for phone number and name until user quits the system. The user can update contact for a user later if they want.

## Information the system needs ##

**Inputs** --> (a).Name (b).Phone_number
**What program stores** --> a dictionary contacts = {}
**Outputs** --> What the systems prints out eg Total number of contacts.

## Rules ##

**Option 1 (add):** -> User is asked to input name he may enter names that aren't valid values e.g BINKA fully capital so built in functions eg ,Binka or Halima are accepted use `.title()`
`.strip()` and `.lower()` and `.isalpha()` and `.replace(" " ,"")` is used to clean the name.Name is fully words no numbers and User then is asked to enter phone number which must be digits and exactly 10 digits.

**Option 2 (Find):** Cleans input name. Prints number if found, otherwise prints "Contact not found".

**Option 3 (Delete):** Cleans input name. Removes contact if found, otherwise prints "Contact not found".

**Option 4 (Update)** Asks user for name if it exists user can later write a new number and it will override the first number 

**Option 5 (Show All):** Prints all contacts. If dictionary is empty, prints "No contacts saved yet".

**Option 6 (Quit):** Breaks the loop and exits the system.

Dictionary holds key and value key = name , value = phone number.


## What could go wrong ##

**Empty types**
1.User may leave name input as empty.
2.User may leave number input as empty.

**Invalid Types**
1.User may try to enter number instead of words for name. (Invalid! Name can only be words.)
2.User may try to enter words instead of number for phone_number.(Invalid! phone number can only be digits.)
3.Updating a phone number with non-digit value should reject and return error message and not update the contact.("Enter valid phone number!")

**Out of range types**
1.User may enter number which is more than 10 digits.(phone number must be exactly 10 digits.)

**duplicate data types**
1.User may try to find contact that isn't stored.
2.User may try to add a contact that already exists.(Contact already exists!)

**Mising types**
1.User may try to delete contact that isn't stored or find a contact that isn't stored. (Contact not found!).
2.User may try to update a contact that isn't in the contact list.


**Empty list on show all**
1.Print "No contact found"

**Invalid menu choice:** 
1.Print "Invalid choice. Please pick 1–6." and redisplay the menu.

