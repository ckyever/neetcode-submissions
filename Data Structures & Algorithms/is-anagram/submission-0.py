class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        for char in s:
            if char in sChars:
                sChars[char] += 1
            else:
                sChars[char] = 1

        for char in t:
            if char in sChars:
                if sChars[char] == 1:
                    del sChars[char]
                else:
                    sChars[char] -= 1
            else:
                return False

        if len(sChars) == 0:
            return True
        else:
            return False

