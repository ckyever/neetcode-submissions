class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        lastIndex = len(nums) - 1
        dp[lastIndex] = 1
        bestLIS = 1

        for i in range(lastIndex-1, -1, -1):
            currentNum = nums[i]
            maxLIS = 1
            for j in range(i+1, len(nums)):
                if currentNum < nums[j]:
                    maxLIS = max(maxLIS, dp[j]+1)
            dp[i] = maxLIS
            bestLIS = max(bestLIS, maxLIS)
        
        return bestLIS