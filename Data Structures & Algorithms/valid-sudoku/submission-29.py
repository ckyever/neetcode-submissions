class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                boxKey = f"{r//3},{c//3}"
                currentNumber = board[r][c]

                if (currentNumber in rows[r]
                    or currentNumber in cols[c]
                    or currentNumber in boxes[boxKey]
                ):
                    return False
                else:
                    rows[r].add(currentNumber)
                    cols[c].add(currentNumber)
                    boxes[boxKey].add(currentNumber)
                    
        return True


        