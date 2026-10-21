def count_letters(word):

    words = {}

    for letter in word:
        words[letter] = words.get(letter, 0) + 1
    return words

def valid_anagram(word1,word2):
    return count_letters(word1) == count_letters(word2)

print(valid_anagram("silent","listen"))
print(valid_anagram("cat","rat"))
print(valid_anagram("aab","abb"))
print(valid_anagram(" "," "))
