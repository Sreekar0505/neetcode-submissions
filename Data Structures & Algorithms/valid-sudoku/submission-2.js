class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidRow(row, board) {
        const count = Array(9).fill(0)
        for (let j=0; j<9; j++) {
            if (board[row][j] !== '.') {
                count[Number(board[row][j])-1]++
            }
        }
        for (const val of count) {
            if (val > 1) return false;
        }
        return true;
    }

    isValidCol(col, board) {
        const count = Array(9).fill(0)
        for (let i=0; i<9; i++) {
            if (board[i][col] !== '.') {
                count[Number(board[i][col])-1]++
            }
        }
        for (const val of count) {
            if (val > 1) return false;
        }
        return true;
    }

    isValidGrid(num, board) {
        const row = Math.floor(num/3), col =  num%3;
        const count = Array(9).fill(0)
        for (let i=row*3; i<(row+1)*3; i++) {
            for (let j=col*3; j<(col+1)*3; j++){
                if (board[i][j] !== '.') {
                    count[Number(board[i][j])-1]++
                }
            }
        }
        for (const val of count) {
            if (val > 1) return false;
        }
        return true;
    }

    isValidSudoku(board) {
        let flag = true
        for (let i=0; i<9; i++) {
            flag = flag && this.isValidRow(i,board) 
                        && this.isValidCol(i,board)
                        && this.isValidGrid(i,board)
        }
        return flag 
    }
}
