## Day 3: Running Sum of 1d Array ## 

**Problem** Taking a list of numbers `(eg [1,2,3,4])` and returning a summed list `(eg [1,2,6,10])`

**My plan** Moving forward the list remembers the prevous number and adds to the current number, It starts from the number the very first index of the list `index 0` and adds to the number of `index 1` and for each round u keep adding the current number.

**Tests**

`print(running_sum(numbers))` numbers = [1,2,3,4] *out come - [1,3,6,10]* 

`print(running_sum([5]))` *outcome - [5]*

`print(running_sum([3,-1,2]))` *outcome = [3, 2, 4]*

`print(running_sum([]))` *outcome = []*

**What tripped Me** 

When i was returning i indented the `return sum_total` inside the for loop and i wasn't getting the correct out come for example for `numbers = [1,2,3,4]` i was getting only 1, from the print() so i figured it out and was able to solve. 

**Pattern** 

Keep a running state variable, update it on each item as you iterate, and save or return the intermediate result at every step.


