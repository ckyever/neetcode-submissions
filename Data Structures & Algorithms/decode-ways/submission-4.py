class Solution:
    def numDecodings(self, s: str) -> int:
        self.count = 0
        dp = {len(s) : 1}
        def dfs(index: int) -> None:
            if index in dp:
                # Already cached the solution for this substring
                return dp[index]
            if s[index] == '0':
                # This substring is not valid
                return 0
            
            # Explore single digit grouping
            result = dfs(index + 1)
            
            # Explore two digit grouping if it exists
            if (index + 2) <= len(s):
                if int(s[index: index+2]) <= 26:
                    result += dfs(index + 2)
            dp[index] = result
            return result
            
        return dfs(0)