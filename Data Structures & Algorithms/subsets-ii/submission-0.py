class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(subset: List[int], index: int):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            current_num = nums[index]
            subset.append(nums[index])
            dfs(subset, index+1)
            subset.pop()

            # We don't want to include this number at all so skip duplicates
            while index < len(nums) and nums[index] == current_num:
                index += 1
            dfs(subset, index)
            
        dfs([], 0)

        return result