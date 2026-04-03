class Solution:
    NUMBER_TRACKER = [0] * 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.NUMBER_TRACKER = [0] * 9

        if not self.isValidRows(board):
            return False

        if not self.isValidColumns(board):
            return False

        if not self.isValidSubBoxes(board):
            return False

        return True

    def isValidRows(self, board: List[List[str]]) -> bool:

        for row in board:
            for number in row:
                i = self.getNumberTrackerIndex(number)
                if i >= 0:
                    self.NUMBER_TRACKER[i] += 1
            if not self.isNumberTrackerValid():
                return False

        return True

    def isValidColumns(self, board: List[List[str]]) -> bool:
        for index in range(9):
            for row in board:
                i = self.getNumberTrackerIndex(row[index])
                if i >= 0:
                    self.NUMBER_TRACKER[i] += 1
            if not self.isNumberTrackerValid():
                return False
                
        return True


    def isValidSubBoxes(self, board: List[List[str]]) -> bool:
        for rowStartIndex in range(0,7,3):
            for columnStartIndex in range(0,7,3):
                for rowIndex in range(rowStartIndex, rowStartIndex+3):
                    # Actual column index
                    for columnIndex in range(columnStartIndex, columnStartIndex+3):
                            i = self.getNumberTrackerIndex(board[rowIndex][columnIndex])
                            if i >= 0:
                                self.NUMBER_TRACKER[i] += 1

                # We have gone through the sub-box
                if not self.isNumberTrackerValid():
                    return False

        return True
    
    # Always reset number tracker after validating it
    def isNumberTrackerValid(self) -> bool:
        for i, number in enumerate(self.NUMBER_TRACKER):
            if number > 1:
                self.NUMBER_TRACKER = [0] * 9
                return False

        self.NUMBER_TRACKER = [0] * 9
        return True

    # If square is blank ('.') return -1
    def getNumberTrackerIndex(self, square: str) -> int:
        try:
            i = int(square) - 1
        except ValueError:
            i = -1
        
        return i
