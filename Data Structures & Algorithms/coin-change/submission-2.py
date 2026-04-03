class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(total: int) -> int:
            if total in dp:
                return dp[total]
            
            if total == amount:
                return 0

            if total > amount:
                return -1

            result = amount + 1
            for coin in coins:
                n = dfs(total + coin)
                if n != -1:
                    result = min(result, n+1)

            # Result hasn't changed from initial value so no possible solution
            if result == amount + 1:
                result = -1

            dp[total] = result
            return result

        return dfs(0)
