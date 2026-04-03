class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while numbers[left_index] + numbers[right_index] != target:
            if left_index >= right_index:
                left_index = 0
                right_index -= 1
                continue

            if numbers[left_index] + numbers[right_index] > target:
                right_index -= 1
            else:
                left_index += 1

        return [left_index+1, right_index+1]
        