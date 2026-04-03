class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinctNums = {}
        for num in nums:
            if num in distinctNums:
                return True
            else:
                distinctNums[num] = num
        return False
         