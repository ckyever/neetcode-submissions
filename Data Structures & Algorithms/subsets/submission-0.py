class Solution:
    def convert_subset_to_key(self, nums: List[int]) -> str:
        return ",".join([str(n) for n in nums])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = {}

        def getSubset(nums: List[int]):
            result[self.convert_subset_to_key(nums)] = nums

            if nums:
                # Recursively call but with one number removed from current nums
                for num_to_remove in nums:
                    next_subset = [n for n in nums if n != num_to_remove]
                    if self.convert_subset_to_key(next_subset) not in result:
                        # Only explore subset if it is unique
                        getSubset(next_subset)

        getSubset(nums)

        return [subset for subset in result.values()]

            

            
