class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.target = sum(nums)/2

        def dfs(index: int, total: int) -> bool:
            if total == self.target:
                return True

            if total > self.target or index >= len(nums):
                return False

            # We can either add or ignore the current number for the subset
            return dfs(index+1, total + nums[index]) or dfs(index+1, total)
        
        return dfs(0, 0)