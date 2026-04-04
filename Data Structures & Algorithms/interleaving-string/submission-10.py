class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lengthS1 = len(s1)
        lengthS2 = len(s2)

        if (lengthS1 + lengthS2) != len(s3):
            return False 

        dp = []
        for i in range(lengthS2+1):
            dp.append([False for j in range(lengthS1+1)])

        dp[lengthS2][lengthS1] = True
        
        for i in range(lengthS2, -1, -1):
            for j in range(lengthS1, -1, -1):
                if i < lengthS2 and s2[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < lengthS1 and s1[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]


