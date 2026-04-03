class Solution:
    def findMin(self, nums: List[int]) -> int:   
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        min_value = math.inf

        while left <= right:
            if left == right:
                min_value = min(min_value, nums[left])

            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                # Min value is on left (including middle)
                right = mid
            else:
                # Min value is on right or is this current left value (so store it)
                min_value = min(min_value, nums[left])
                left = mid + 1

        return min_value


