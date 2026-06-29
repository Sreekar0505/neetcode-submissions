class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        x,y = 0,(m*n)-1

        while x<=y:
            mid = (x+y) // 2
            if matrix[mid//m][mid%m] == target:
                return True
            elif matrix[mid//m][mid%m] < target: x = mid+1
            else: y = mid-1
        return False