## Day-4 Checking for Contains Duplicate ##

**Problem** - Checking through a list of numbbers eg `[1,2,3,1]` and checking a number appears twice.returns `True` if it's there and returns `False` if not there. 

**My plan** - Going from first number to the last each time i move from a number i remeber it and ask did i see this if yes return `True` if no continue until the end and return `False`

**Tests**

`print(check_duplicate_numbers(numbers))` numbers = [1,2,3,4,1] *outcome = True*

`print(check_duplicate_numbers([1,2,3]))` *outcome = False*

`print(check_duplicate_numbers([]))` *outcome = False*

`print(check_duplicate_numbers([5]))` *outcome = False*

**What tripped me**

Instead of appending `number` into `duplicate_num` list i was returning the `duplicate_num` list itself.

**patern**

Keep iterating through the list each time you see a number remeber it the next time you see a number like the one you remeber return True.

