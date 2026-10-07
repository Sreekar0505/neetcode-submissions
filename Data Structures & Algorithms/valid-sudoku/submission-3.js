class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const checkRow = (row) => {
            const dist = {}
            for (let i=0; i<9; i++) {
                if (board[row][i] !== '.'){
                    if (Object.hasOwn(dist,board[row][i])){
                        dist[board[row][i]]++;
                    } else {
                        dist[board[row][i]] = 1
                    }
                }
            }
            for (const [key,value] of Object.entries(dist)){
                if (value > 1) return false
            }
            return true
        }

        const checkCol = (col) => {
            const dist = {}
            for (let i=0; i<9; i++) {
                if (board[i][col] !== '.'){
                    if (Object.hasOwn(dist,board[i][col])){
                        dist[board[i][col]]++;
                    } else {
                        dist[board[i][col]] = 1
                    }
                }
            }
            for (const [key,value] of Object.entries(dist)){
                if (value > 1) return false
            }
            return true
        }

        const checkGrid = (x,y) => {
            const dist = {}
            for (let i=3*x; i<(3*x) + 3; i++) {
                for (let j=3*y; j<(3*y) +3; j++) {
                    if (board[i][j] !== '.'){
                        if (Object.hasOwn(dist,board[i][j])){
                            dist[board[i][j]]++;
                        } else {
                            dist[board[i][j]] = 1
                        }
                    }
                }
            }
            for (const [key,value] of Object.entries(dist)){
                if (value > 1) return false
            }
            return true
        }

        for (let i=0; i<9; i++) {
            if (!checkRow(i) || !(checkCol(i)) || !(checkGrid(Math.floor(i/3),i%3))) return false
        }


        return true
    }
}
