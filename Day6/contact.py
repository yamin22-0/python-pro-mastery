#TODO: (add) ->Ask user for Name.
#TODO: (add) ->Ask user for phone number.
#TODO: Validate if there's any empty inputs for name or number.
#TODO: Validate if name is words not symbol or numbers. 
#TODO: Validate if number is not words and is strictly 10 digits.
#TODO: Print contact_list
#TODO: (Find) --> Cleans input name,remove spaces and prints the contact if
#                  found.Otherwise if contact not found prints (contact not found)
#TODO: (Delete) --> Deletes contact if found, if not found prints (contact not found).
#TODO: (Update) --> Updates number to a contact that was added in (add contact) feature.
#TODO: (Show all) --> prints all contacts if dictionary empty prints "No contacts found".
#TODO: (Quit) --> Break the loop and exits the system.


def contact_book():

    contact_list = {}

    while True:
        print("\n##-- contact book --##")
        print("1. Add contact.")
        print("2. Find contact.")
        print("3. Delete contact.")
        print("4. Update contact.")
        print("5. Show all contacts.")
        print("6. Quit.")

        choice = input("Choose option: ").strip()

        if choice == "1":
            raw_name = input("Enter name: ")
            clean_name = raw_name.strip().lower()

            if clean_name in contact_list:
                print("Contact already exists.")
                continue
            elif not clean_name.replace(" ","").isalpha():
                print("Enter valid name.")
                continue
            else:
                print("Contact name saved succesfully.")
                

            raw_phone = input("Enter phone number: ")
            clean_phone = raw_phone.strip()

            if len(clean_phone) != 10 or not clean_phone.isdigit():
                print("Enter correct number.")
                continue
            else:
                print("Contact saved successfully.")

            contact_list[clean_name] = clean_phone
            print(f"Contact added: {clean_name.title()} : {clean_phone}")

        elif choice == "2":
            raw_find = input("Search for Contacts: ")
            clean_find = raw_find.strip().lower()

            if not clean_find:
                print("Please enter name to search!")
                continue

            found = 0

            for name,phone in contact_list.items():
                if clean_find in name:
                    print(f"Found: {name.title()} -> {phone}")
                    found += 1

            if clean_find in contact_list:
                phone = contact_list[clean_find]
                print(f"Found: {clean_find.title()} -> {phone}")

            if found == 0:
                print("Contact not found.")

        elif choice == "3":
            raw_delete = input("Delete contact: ")
            clean_delete = raw_delete.strip().lower()

            if clean_delete in contact_list:
                del contact_list[clean_delete]
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")


        elif choice == "4":
            raw_update = input("Update contact: ")
            clean_update = raw_update.strip().lower()

            if clean_update not in contact_list:
                print("Contact not found")
                continue

            new_phone = input("Enter new phone number: ").strip()

            if len(new_phone) != 10 or not new_phone.isdigit():
                print("Enter correct number!")
                continue
               
            contact_list[clean_update] = new_phone
            print("Number updated successfully.")

        elif choice == "5":
            if not contact_list:
                print("No contacts saved yet.")
            else:
                print("\n## -- saved contacts --##")

                for name,phone in contact_list.items():
                    print(f"Contacts : {name.title()} - {phone}")

        elif choice == "6":
            confirm = input("Are you sure you want to quit? (Yes/no): ").strip().lower()

            if confirm == "yes":
                print("Exitng contact book.")
                break

        else:
            print("Enter valid option")
            

contact_book()





