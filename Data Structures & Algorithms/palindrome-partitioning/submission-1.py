class Solution:
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        substrings = []

        def dfs(i: int):
            if i >= len(s):
                result.append(substrings.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    substrings.append(s[i:j+1])
                    dfs(j + 1)
                    substrings.pop()
        
        dfs(0)
        return result