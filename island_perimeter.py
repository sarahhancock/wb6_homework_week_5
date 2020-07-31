class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            u = 1 if i > 0 and grid[i - 1][j]==1 else 0
            d = 1 if i < m-1 and grid[i + 1][j]==1 else 0
            l = 1 if j > 0 and grid[i][j - 1]==1 else 0
            r = 1 if j < n-1 and grid[i][j + 1]==1 else 0
            return 4-u-d-l-r
            
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    perimeter += dfs(i,j)
        return perimeter