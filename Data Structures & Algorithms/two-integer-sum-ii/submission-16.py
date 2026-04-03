class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        # Sum these two pointers
        # If sum is = target
            # Return index
        # Elif sum is > target
            # Move right pointer down
        # Elif sum is < target
            # Move left pointer up

        left = 0
        right = len(numbers) - 1

        while True:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        raise Exception("No solution for these numbers")
            