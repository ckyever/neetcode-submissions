from collections import defaultdict



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedStrings = {}
        for string in strs:
            sortedChars = sorted(string)
            sortedString = "".join(sortedChars)
            if sortedString in groupedStrings:
                groupedStrings[sortedString].append(string)
            else:
                groupedStrings[sortedString] = [string]
        
        sublists = []
        for groups in groupedStrings.values():
            print(groups)
            sublists.append(groups)
        print(sublists)

        return sublists
