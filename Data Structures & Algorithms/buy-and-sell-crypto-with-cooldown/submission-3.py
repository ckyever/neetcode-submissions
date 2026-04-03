class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #<(day, buy_or_sell): max_profit>

        def dfs(day: int, isBuying: bool):
            if day >= len(prices):
                return 0

            if (day, isBuying) in dp:
                return dp[(day, isBuying)]

            if isBuying:
                buy = dfs(day + 1, not isBuying) - prices[day]
                cooldown = dfs(day + 1, isBuying)
                dp[(day, isBuying)] = max(buy, cooldown)
            else:
                sell = dfs(day + 2, not isBuying) + prices[day]
                cooldown = dfs(day + 1, isBuying)
                dp[(day, isBuying)] = max(sell, cooldown)

            return dp[(day, isBuying)]

        return dfs(0, True)
        
