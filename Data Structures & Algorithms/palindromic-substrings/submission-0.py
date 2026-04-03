class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        for i in range(len(s)):

            def findPalindromes(left: int, right: int):
                while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                    left -= 1
                    right += 1
                    self.count += 1

            # Check for odd length palindrome
            findPalindromes(i, i)

            # Check for even length palindrome
            findPalindromes(i, i+1)


        return self.count