class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        dp = {}
        def dfs(index: int) -> bool:
            if index in dp:
                return dp[index]
                
            if index >= len(s):
                return True
            
            foundSolution = False
            for word in wordDict:
                endIndex = len(word)
                if s[index:index+endIndex] == word:
                    dp[index] = dfs(index+endIndex)
                    if dp[index]:
                        foundSolution = True
            
            return foundSolution
        
        return dfs(0)