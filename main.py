# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    
        # [assignment] Add your code here
    if(sorted(word1) == sorted(word2)):
            print(sorted(word1),sorted(word2))
            return True
    return False
    

print(find_anagrams('listen' , 'silent'))
    

