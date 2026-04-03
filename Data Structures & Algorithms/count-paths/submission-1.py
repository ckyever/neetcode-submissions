class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for row in range(m):
            dp.append([0] * n)

        dp[m-1][n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row == m-1 and col == n-1:
                    # We already set a value for finish
                    continue
                
                # Get value from cell below if possible
                if row + 1 < m:
                    dp[row][col] += dp[row+1][col]

                # Get value from cell on the right if possible
                if col + 1 < n:
                    dp[row][col] += dp[row][col+1]
        
        return dp[0][0]

