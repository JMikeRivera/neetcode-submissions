class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            count = [0] * 26

            for letter in word:
                index = ord(letter) - ord("a")
                count[index] += 1

            key = tuple(count)

            if key not in dictionary:
                dictionary[key] = []

            dictionary[key].append(word)

        return list(dictionary.values())
        
        