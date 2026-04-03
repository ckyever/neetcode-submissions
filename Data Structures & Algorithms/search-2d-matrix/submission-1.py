class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][0] <= target:
                # Must be in this row
                for num in matrix[i]:
                    if num == target:
                        return True
                # Number is not in row hence not in matrix
                return False   

        return False  