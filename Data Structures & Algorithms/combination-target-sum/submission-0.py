class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:    
        result = []

        def dfs(i: int, combo: List[int]):
            total = sum(combo)
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target or i >= len(nums):
                return

            combo.append(nums[i])
            # Add the previous number to combo
            dfs(i, combo)
            combo.pop()

            # Add the next number in nums to combo
            dfs(i+1, combo)

        dfs(0, [])
        return result

