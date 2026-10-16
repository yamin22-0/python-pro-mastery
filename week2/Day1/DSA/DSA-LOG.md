## Day 1 find_largest(10/10/2026) ##

**Problem** - Returning the largest number in a list.without using `max()`.
**My plan (my words)** - remember the biggest so far, look at each number, replace it when I meet a bigger one. 
**Tests** 
`print(find_largest(([2,3,9])))`
`print(find_largest(([-5,-1,-9])))`
`print(find_largest(([7])))`

**What tripped me** 

Using position `numbers` instead of value `[0]` - I wrote numbers[number], but the brackets need a position (0, 1, 2), not a value. numbers[0] is the first item.

`largest + 1` adds 1 and throws the answer away. What I needed was `largest = number`, which replaces the remembered number with the bigger one.

**What i learnt**

I can find largest number in a list without using `max() method`.Honeslty i never knew something like this exists. So the first step is initialising largest `(largest = numbers[0])`. U now use `for` loop to loop through and find the largest number 
