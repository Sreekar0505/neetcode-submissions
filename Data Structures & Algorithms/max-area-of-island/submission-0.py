class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n,m = len(grid), len(grid[0])

        visited = [[0]*m for _ in range(n)]

        def dfs(x,y):
            if grid[x][y] == 0 or visited[x][y] == 1:
                return 0
            visited[x][y] = 1
            area = 1

            for i,j in [(0,1),(1,0),(0,-1), (-1,0)]:
                if x+i<n and x+i>=0 and y+j<m and y+j>=0:
                    area += dfs(x+i,y+j)
            return area
        
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))
        return ans
