class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row):
            hashset = {}
            for i in range(9):
                if (board[row][i] != '.'):
                    hashset[board[row][i]] = hashset.get(board[row][i],0) + 1
            for val in hashset.values():
                if val > 1:
                    return False
            return True
        
        def checkCol(col):
            hashset = {}
            for i in range(9):
                if (board[i][col] != '.'):
                    hashset[board[i][col]] = hashset.get(board[i][col],0) + 1
            for val in hashset.values():
                if val > 1:
                    return False
            return True

        def checkGrid(row,col):
            hashset = {}
            for i in range(3):
                for j in range(3):
                    if (board[(row*3)+i][(col*3)+j] != '.'):
                        hashset[board[(row*3)+i][(col*3)+j]] = hashset.get(board[(row*3)+i][(col*3)+j],0) + 1
            for val in hashset.values():
                if val > 1:
                    return False
            return True

        for i in range(9):
            if (checkRow(i) == False or checkCol(i) == False or checkGrid(i%3,i//3) == False):
                return False
        return True


