class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        for i in range(len(nums)):
            if i == 0:
                continue
            
            if i == 1:
                nums[i] = max(nums[i-1], nums[i])
                continue

            newTotal = nums[i] + nums[i-2]
            nums[i] = max(newTotal, nums[i-1])

        return max(nums[-1], nums[-2])

        