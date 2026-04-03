class Solution:
    def binarySearch(self, nums: List[int], target: int, first_index: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return first_index
            else:
                return -1
        
        mid_point_index = len(nums) // 2

        if nums[mid_point_index] == target:
            return first_index + mid_point_index

        if nums[mid_point_index] > target:
            return self.binarySearch(nums[:mid_point_index], target, first_index)
        else:
            new_first_index = first_index + mid_point_index + 1
            return self.binarySearch(nums[mid_point_index+1:], target, new_first_index)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0)

        
        
        