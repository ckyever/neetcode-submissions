class Solution:
    def convertStringToDictionary(self, string: str) -> dict:
        dictionary = {}
        for char in string:
            if char in dictionary:
                dictionary[char] = dictionary[char] + 1
            else:
                dictionary[char] = 1
        return dictionary

    def isAnagram(self, s: str, t: str) -> bool:
        sDictionary = self.convertStringToDictionary(s)
        tDictionary = self.convertStringToDictionary(t)

        return sDictionary == tDictionary
