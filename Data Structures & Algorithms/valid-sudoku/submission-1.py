class Solution:
    def checkRows(self, board):
        for row in board:
            freq = [0]*9
            for i in row:
                if i != '.' and freq[int(i)-1] > 0:
                    return False
                elif i != '.':
                    freq[int(i)-1]+=1
        return True
    
    def checkCols(self, board):
        for j in range(9):
            freq = [0]*9
            for i in range(9):
                if board[i][j] != '.' and freq[int(board[i][j]) - 1] > 0:
                    return False
                elif board[i][j] != '.':
                    freq[int(board[i][j])-1]+=1
        return True

    def checkGrids(self, board):
        for i in range(3):
            for j in range(3):
                freq = [0]*9
                for x in range(i*3,(i*3) + 3):
                    for y in range(j*3, (j*3) + 3):
                        if board[x][y] != '.' and freq[int(board[x][y]) - 1] > 0:
                            return False
                        elif board[x][y] != '.':
                            freq[int(board[x][y]) - 1]+=1
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkGrids(board)