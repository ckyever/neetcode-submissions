class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target: 
                return right

            mid = (left + right) // 2
            print(f"{nums[left]}-{nums[mid]}-{nums[right]}")

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1