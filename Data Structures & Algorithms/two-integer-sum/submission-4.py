class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6]

        #2 Loop through each nums and find complement to reach target, then loop through this to see if it exists in nums

        # Loop through nums
            # Target - num = complement
            # If complement in hashset
                # Return indexes
            # Store complement in hashmap with key: num value: index

        # Raise error

        complements = {}

        for index, n in enumerate(nums):
            complement = target - n

            if complement in complements:
                return [complements[complement], index]
            
            complements[n] = index

        raise Exception("No possible solution")