class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        island = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=column or grid[r][c] == '0':
                return False
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for i in range(row):
            for j in range(column):
                if grid[i][j]=='1':
                    island+=1
                    dfs(i,j)
        return island
        