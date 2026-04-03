class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # This holds the max totals as we backtrack up the decision tree
        totals = nums[:]

        for i in range(len(nums)-1, -1, -1):
            if (i-2) >= 0:
                new_total = totals[i] + nums[i-2]
                totals[i-2] = max(new_total, totals[i-2])
            if (i-3) >= 0:
                new_total = totals[i] + nums[i-3]
                totals[i-3] = max(new_total, totals[i-3])

        return max(totals[0], totals[1])
        
        