class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIndex = 0
        endIndex = len(s) - 1

        while startIndex <= endIndex:
            if not s[startIndex].isalnum():
                startIndex += 1
                continue
            if not s[endIndex].isalnum():
                endIndex -= 1
                continue
            
            if s[startIndex].lower() == s[endIndex].lower():
                startIndex += 1
                endIndex -= 1
            else:
                return False

        return True
            
        