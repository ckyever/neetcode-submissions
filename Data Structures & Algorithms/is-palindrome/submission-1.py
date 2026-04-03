class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Corner cases:
        # a = True
        # abba = True (even length)
        # aba = True (odd length)

        leftIndex = 0
        rightIndex = len(s)-1

        while leftIndex <= rightIndex:
            if not s[leftIndex].isalnum():
                leftIndex += 1
                continue

            if not s[rightIndex].isalnum():
                rightIndex -= 1
                continue

            if s[leftIndex].lower() == s[rightIndex].lower():
                leftIndex += 1
                rightIndex -= 1
            else:
                return False
            
        return True


