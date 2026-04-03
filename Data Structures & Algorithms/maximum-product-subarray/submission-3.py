class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        currentMax = 1
        currentMin = 1

        for n in nums:
            temp = currentMax * n
            currentMax = max(temp, currentMin * n, n)
            currentMin = min(temp, currentMin * n, n)
            maxProduct = max(maxProduct, currentMax)

        return maxProduct
