class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total)
        
        def dfs(index: int, total: int) -> int:
            if (index, total) in dp:
                return dp[(index,total)]

            if index == len(nums):
                return 1 if total == target else 0

            waysIfWeAdd = dfs(index + 1, total + nums[index])
            waysIfWeMinus = dfs(index + 1, total - nums[index])

            dp[(index,total)] = waysIfWeAdd + waysIfWeMinus

            return dp[(index,total)]

        return dfs(0, 0)
