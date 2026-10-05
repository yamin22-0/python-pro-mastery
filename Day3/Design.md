## What the system does ## 
This is a sphopping list where the system ask the user to enter 3 items that they want to buy. The user enters the 3 items they want to purchase it's appended in a list. The user can later delete.

## what info the system needs ##

(a).items_to_buy  (b).items_to_remove (c).items_list=[#items appended enter here.]  (d).number_of_items


## Rules of the system ##

1.The system ask user for 3 items, it uses while loop to keep asking user until 3 valid items are gotten.while len(items_list) < 3. example --> add : bread,sugar,salt  remove : salt

2.How to get number of items, number_of_items = len(items_list).

3.spaces inside an item are allowed (sugar cane is fine), since the code accepts them.

## What could go wrong ## 

1.User may type number as an item to add, Item can only be words and numbers eg 7up, 2litresmilk. (Invalid! Enter valid item.) the loop re-repeats after the error messages until a valid item is kept.
2.User may leave the add item as empty.(Invalid! Enter valid Item can't be empty:). the loop keeps repeating also if input is empty until 3 items are gotten. 
3.User may type remove item as a number and user may try to remove items that aren't in the items_list=[]
4.User may try to enter an item already in the list(Item exists! Enter item.)
5.If user enters Milk or MILK using .strip.lower makes sure all letters are small leters.




