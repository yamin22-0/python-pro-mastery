## Week 3, Day 3: Balanced Brackets
**Problem:** a string of only opening `(` and closing `)` goes in, returns `True` if balancing or returns False if unbalanced.
**My plan:** ...

-IIterate through each character left to right add 1 when u see a `(` and subtract 1 if `)`.Check if it drops below 0 `return False`.At the end check count if it's exactly 0.

**Tests:** 

-`"(())"` -> `True`
-`"(()"` -> `False`
-`")("` -> `False`
-`"()()"` -> `True`
-`""` -> `True`
-`"((("` -> `False`

**What tripped me:** 

The first time i used `return True` instead of `return count == 0` which made every test return True so i changed it to return count == 0
and each test started returning correct answers.

**Pattern:** 

-Keep a running count. 
-Check it on every step 
-Check it at the end.