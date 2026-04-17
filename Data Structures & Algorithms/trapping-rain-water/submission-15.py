class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        totalWater = 0

        while right > left:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                totalWater += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                totalWater += maxRight - height[right]

        return totalWater