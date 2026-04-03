class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index: int, total: int) -> int:
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            waysIfWeAdd = dfs(index + 1, total + nums[index])
            waysIfWeMinus = dfs(index + 1, total - nums[index])

            return waysIfWeAdd + waysIfWeMinus

        return dfs(0, 0)
