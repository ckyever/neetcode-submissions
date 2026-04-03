class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}

        for string in strs:
            characterCount = {}
            for charInt in range(97, 123):
                characterCount[chr(charInt)] = 0
            for character in string.lower():
                characterCount[character] += 1
            key = str(characterCount)
            print(key)
            
            if key in sublists:
                sublists[key].append(string)
            else:
                sublists[key] = [string]

        groupedStrings = []
        for list in sublists.values():
            groupedStrings.append(list)

        return groupedStrings