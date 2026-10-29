def valid_palindrome(word):

    right =len(word) -1
    left = 0

    while left < right:
        if word[left] != word[right]:
            return False
        right -= 1
        left += 1
    return True

print(valid_palindrome("racecar"))
print(valid_palindrome("abca"))
print(valid_palindrome("abba"))
print(valid_palindrome("a"))
