## Day-6 Return most common item in a list ##

**Problem** - Check through a list of items, return a dictionary of counts of each item then gives the most common item.

**My plan** - First create a count_items(items) function to count each items in a list how many times they appear then use another function to return the most common item in the list.

**Tests**

`print(count_items(counted_items))` counted_items = ["a","b","c","a","b","a","a"] *outcome = {'a': 4, 'b': 2, 'c': 1}*

`print(count_items([]))` *outcome = {}* 

`print(count_items(["x","y"]))` *outcome = {'x': 1, 'y': 1}*

`print(count_items(["x","y","y"]))` *outcome = {'x': 1, 'y': 2}*

`print(most_common(counted_items))` counted_items = ["a","b","c","a","b","a","a"] *outcome = a*

`print(most_common([]))` *outcome = None*

`print(most_common(["x","y"]))` *outcome = x*

`print(most_common(["x","y","y"]))` *outcome = y*

**What tripped me**

Trying to write one function to handle all the logic instead of using a helper function.

**Pattern**

Using `.get(key, 0) + 1` to count total times an item appear in eah list then find the most appearing item on the list using `.items()`.
