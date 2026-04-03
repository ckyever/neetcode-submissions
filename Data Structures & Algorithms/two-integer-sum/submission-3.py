class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for firstIndex, firstNumber in enumerate(nums):
            secondNumber = target - firstNumber
            try:
                secondIndex = nums.index(secondNumber, firstIndex+1)
                return [firstIndex, secondIndex]
            except:
                continue

        return [None, None]
            
        