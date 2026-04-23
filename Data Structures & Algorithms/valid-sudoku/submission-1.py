class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = {}
        colDict = {}
        boxDict = {}
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue

                d = board[row][col]
                v_in_r = (row, d)
                v_in_c = (col, d)

                boxIndex = (row // 3) * 3 + (col // 3)
                v_in_b = (boxIndex, d)

                if v_in_r in rowDict or v_in_c in colDict or v_in_b in boxDict:
                    return False
                
                rowDict[v_in_r] = 1
                colDict[v_in_c] = 1
                boxDict[v_in_b] = 1
        
        return True