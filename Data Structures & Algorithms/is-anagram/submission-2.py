class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        # fill the letters dictionary
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        # empty the letters dictionary
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
            else: return False
        
        print(letters)
        return all(letter == 0 for letter in letters.values())