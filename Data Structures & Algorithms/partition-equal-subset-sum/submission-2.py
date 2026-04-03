class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subsetSums = {0}
        target = sum(nums)/2

        for i in range(len(nums)-1, -1, -1):
            newSubsetSums = set()
            for s in subsetSums:
                newSubsetSums.add(s)
                newSum = s+nums[i]
                if newSum == target:
                    return True
                newSubsetSums.add(newSum)
            subsetSums = newSubsetSums
        
        return False

        