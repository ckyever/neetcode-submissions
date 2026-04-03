class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # init dp same length as nums
        # last dp value is 1
        # keep track of largest dp value

        # backwards iterate nums from second last number
            # find number to the right that is greater than it
            # and has the largest dp value
            # if it exists
                # increment that dp value and set as this one
            # else
                # this value is 1
            
        # return largest dp value
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