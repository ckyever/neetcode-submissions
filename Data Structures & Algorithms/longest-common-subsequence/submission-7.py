class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)

        dp = []
        for r in range(rows+1):
            dp.append([0] * (cols+1))

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row][col+1], dp[row+1][col])


        print(dp)
        return dp[0][0]
