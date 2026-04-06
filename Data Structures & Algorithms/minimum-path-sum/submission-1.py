class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)-1
        column = len(grid[0])-1
        mem= {}
        def dfs(i,j):
            if i>row or j>column:
                return float('inf')
            if i == row and j==column:
                return grid[row][column]
            if (i,j) in mem:
                return mem[(i,j)]
            mem[(i,j)] =  grid[i][j]+ min(dfs(i+1,j), dfs(i,j+1))
            return mem[(i,j)]
        return dfs(0,0)


        