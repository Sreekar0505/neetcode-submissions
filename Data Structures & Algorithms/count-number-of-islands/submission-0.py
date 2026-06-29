class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]

        def dfs(x,y):
            if visited[x][y] == 1 or grid[x][y] == '0':
                return
            visited[x][y] = 1
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                if x+i>=0 and x+i<n and y+j>=0 and y+j<m:
                    dfs(x+i,y+j)
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count