class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = {}

        for i in range(len(nums)):
            number = nums[i]
            if number in uniqueNums:
                return True
            else:
                uniqueNums[number] = number
        return False
         