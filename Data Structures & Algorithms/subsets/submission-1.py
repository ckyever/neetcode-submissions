class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index: int, sublist: List[int]) -> List[int]:
            if index == len(nums):
                result.append(sublist)
                return sublist

            next_index = index + 1
            dfs(next_index, sublist)
            dfs(next_index, sublist + [nums[index]])

        dfs(0, [])

        return result