# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1,word2):
    # [assignment] Add your code here
    # sort the strings & compare them
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
print(find_anagrams('secure','rescue'))

