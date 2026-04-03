def isValid(condition: Set[int], number: int) -> bool:
    if number in condition:
        return False
    condition.add(number)
    return True

def getBoxIndex(row: int, col: int) -> int:
    if row >= 0 and row <= 2 and col >= 0 and col <= 2:
        return 0
    elif row >= 0 and row <= 2 and col >= 3 and col <= 5:
        return 1
    elif row >= 0 and row <= 2 and col >= 6 and col <= 8:
        return 2
    elif row >= 3 and row <= 5 and col >= 0 and col <= 2:
        return 3
    elif row >= 3 and row <= 5 and col >= 3 and col <= 5:
        return 4
    elif row >= 3 and row <= 5 and col >= 6 and col <= 8:
        return 5
    elif row >= 6 and row <= 8 and col >= 0 and col <= 2:
        return 6
    elif row >= 6 and row <= 8 and col >= 3 and col <= 5:
        return 7
    elif row >= 6 and row <= 8 and col >= 6 and col <= 8:
        return 8
    else:
        raise Exception(f"Failed to get box index for [{row}, {col}]")


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                boxIndex = getBoxIndex(i, j)

                if not isValid(rows[i], board[i][j]):
                    return False
                elif not isValid(cols[j], board[i][j]):
                    return False
                elif not isValid(boxes[boxIndex], board[i][j]):
                    return False
                    
        return True


        