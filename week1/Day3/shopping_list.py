#TODO: Initialise empty list.
#TODO: Ask user for 3 items using (len(items_list)) until user enters 3 items.
#TODO: Validate and clean inputs with spaces and capital letters. use .strip() and .lower()
#TODO: Validate and reject empty inputs or items that are strictly .isdigit().
#TODO: Append valid items to items_list[].
#TODO: Print final list with the users items
#TODO: Ask user to input item to delete.
#TODO: Validate if item is in list and remove if in list.
#TODO: Print final updated shopping list and the new items count.


def shopping_list():

    items_list = []

    while len(items_list) < 3:
        add_items = input("Enter Item : ").strip().lower()

        if add_items == "":
            print("Invalid! Enter valid Item can't be empty:")
            continue
        elif add_items.isdigit():
            print("Invalid! Enter valid item: ")
            continue
        elif add_items in items_list:
            print("Items exists! Enter item: ")
            continue

        items_list.append(add_items)

    print(items_list)
    print(len(items_list))

    remove_items = input("Enter item to remove :").strip().lower()
            
    if remove_items in items_list:
        items_list.remove(remove_items)
        print("Item removed successfully.")
    else:
        print("Item not found in list.")

    print(items_list)
    print(len(items_list))

shopping_list()
