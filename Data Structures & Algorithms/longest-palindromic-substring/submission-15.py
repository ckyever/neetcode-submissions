class Solution:
    def getPalindromeFromCentre(self, s: str, left: int, right: int, current: str) -> str:
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        # Return the strings just before left and right
        palindrome = s[left+1:right]

        if len(palindrome) > len(current):
            return palindrome
        else:
            return current

    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s)-1):
            if ((i-1) >= 0 and s[i-1] == s[i+1]) or s[i] == s[i+1]:
                # Odd number palindrome
                result = self.getPalindromeFromCentre(s, i-1, i+1, result)

                # Even number palindrome
                result = self.getPalindromeFromCentre(s, i, i+1, result)

        return result