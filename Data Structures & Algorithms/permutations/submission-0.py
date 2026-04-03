class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(permutation: List[int], nums: List[int]):
            if not nums:
                result.append(permutation.copy())
                return

            for n in nums:
                permutation.append(n)
                new_nums = nums.copy()
                new_nums.remove(n)
                dfs(permutation, new_nums)
                permutation.pop()
            
        dfs([], nums)

        return result
        