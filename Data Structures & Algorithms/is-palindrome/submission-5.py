class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Point at start and end of string
        # Move inwards until an alphanumeric character is reached
        # Compare start and end pointer
        # If same continue
        # Else return false

        # Return true

        startIndex = 0
        endIndex = len(s) - 1

        while startIndex <= endIndex and startIndex < len(s) and endIndex >= 0:
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
            
        