## Week 3, Day 1: Two Sum ##

**Problem:** - Iterating through items in a list and getting the two indexes if summed gives me the number of the outcome.

**My plan:** - Iterate through the list subtract the target from every value in the list if the subtraction gives u the target return the index of that value if no values bring target return None.

**Tests:** 

`print(two_sum(numbers,9))``numbers = [2,7,11,15]`  *outcome -> [0, 1]*
`print(two_sum([3,2,4],6))` *outcome -> [1, 2]*
`print(two_sum([3,3],6))` *outcome -> [0, 1]*
`print(two_sum([-1,-2,-3],-5))` *outcome -> [1, 2]*
`print(two_sum([1,2],6))` *outcome -> None*

**What tripped me:** 

Returning the dictionary for the for loop instead of returning None because the check was for if not the two summed numbers indexes within the whole list don't give u outcome should return None not the dictionary.

**Pattern:**

Initialize an empty dictionary(seen = {}) then looping using `emumerate` for finding each position with value then sum each item with the last remeber item if gives u outcome print the two position(indexes) if not give None.
