class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for letter in s:
            if letter not in dictionary:
                dictionary[letter] = 1
            else: 
                dictionary[letter] += 1
        
        print(dictionary)

        for letter in t:
            if letter in dictionary:
                dictionary[letter] -= 1
            else:
                dictionary[letter] = 1

        print(dictionary)
        return(all(value == 0 for value in dictionary.values()))