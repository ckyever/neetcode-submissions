class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        top, bottom = 0, len(matrix) - 1

        print(f"{top} - {bottom}")

        while top <= bottom:
            if top == bottom:
                # Number must be in this row so BST it
                return self.binarySearch(matrix[top], target)

            midpoint = (bottom + top) // 2
            if matrix[midpoint][0] > target:
                # Look at top half
                bottom = midpoint - 1
            elif matrix[midpoint][0] < target:
                if midpoint == (len(matrix) - 1) or matrix[midpoint+1][0] > target:
                    # It must be in this row
                    return self.binarySearch(matrix[midpoint], target)
                else:
                    # Look at bottom half
                    top = midpoint + 1
            else:
                # First element of row is target
                return True
        
        return False