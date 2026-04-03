class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Corner cases:
        # a = True
        # abba = True (even length)
        # aba = True (odd length)

        cleanString = ''.join(char.lower() for char in s if char.isalnum())

        leftIndex = 0
        rightIndex = len(cleanString)-1

        while leftIndex <= rightIndex:
            if cleanString[leftIndex] == cleanString[rightIndex]:
                leftIndex += 1
                rightIndex -= 1
            else:
                return False
            
        return True


