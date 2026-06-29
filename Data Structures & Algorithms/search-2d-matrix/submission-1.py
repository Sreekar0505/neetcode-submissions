class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        x,y = n-1,0

        while x>=0 and y<m:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target: x-=1
            else: y+=1
        return False