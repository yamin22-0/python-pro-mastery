## Day-5 Checking for Valid anagram ##

**Problem** - Returns `True` if both words use exactly the same letters the same number of times, and `False` otherwise (e.g., "silent" and "listen" match, while "cat" and "rat" do not).

**My plan** - Count how many times each letter appears in word 1 using a dictionary, do the same for word 2, and then compare the two dictionaries. If they are equal, return `True`; otherwise, return `False`.

**Tests**

`print(valid_anagram("silent","listen"))` *outcome True*

`print(valid_anagram("cat","rat"))` *outcome False*

`print(valid_anagram("aab","abb"))` *outcome False*

`print(valid_anagram("", ""))` *outcome True (nothing to count, so both dictionaries are {} and equal)*

*(Note on capital letters: Decided that "Listen" and "silent" should not match unless converted to lowercase first).*

**What tripped me**

First I used a for loop twice for word 1 and word 2 and tried to compare them directly, which became too complicated. I learned how to use a **helper function** (like `count_letters`) to handle the repeated job of counting, which makes the main function much cleaner. Other bugs along the way included missing parameters, incorrect bracket syntax, and a counting line that referenced the wrong dictionary.

**Pattern**

Count things with a dictionary and `.get(key, 0) + 1`. To compare two collections, count each, then compare the counts. A helper function for a repeated job can be written once and called twice.