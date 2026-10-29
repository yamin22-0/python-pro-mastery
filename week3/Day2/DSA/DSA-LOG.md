## Week 3, Day 2: Valid palindrome. ##

**Problem:** - Checking if word reads the same forwards and backwards.

**My plan:** - Check the word from both sides (left and right) from left move forward and from right move backwards match the letter of the left side to the one in the right then if they match `return True` if they don't match `return False`.  

**Tests:** 

`print(valid_palindeome("racecar"))`  *outcome -> True*
`print(valid_palindeome("abca"))`  *outcome -> False*
`print(valid_palindeome("abba"))`  *outcome -> True*
`print(valid_palindeome("a"))`  *outcome -> True*

**What tripped me:** 

Not finishing the loop by using `left += 1` and `right -= 1` which would have kept me stuck in an infinite loop.

**Pattern:**

Initialising left = 0 and right = len(word) -1 , run a while loop `while left < right` , compare the letters word[left] != word[right] this means if they dont match return False , then if they match for left move a step forward for right move another step backwards  and once all letters match return True.
