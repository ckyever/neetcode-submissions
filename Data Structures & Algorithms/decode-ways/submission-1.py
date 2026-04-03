class Solution:
    def numDecodings(self, s: str) -> int:
        self.count = 0

        def dfs(index: int) -> None:
            # Used up all digits so we created a valid decoded string
            if index >= len(s):
                self.count += 1
                return

            if s[index] == '0':
                return
            
            # Explore single digit grouping
            dfs(index + 1)
            
            # Explore two digit grouping if it exists
            if (index + 2) <= len(s):
                if int(s[index: index+2]) <= 26:
                    dfs(index + 2)
            
        dfs(0)
        return self.count