class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        max_area = 0
        def helper(i,j):
            if i < 0 or j<0 or i>=row or j>=column or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return (1+ helper(i+1,j)+helper(i-1,j)+helper(i,j+1)+
            helper(i,j-1))
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    max_area = max(max_area,helper(i,j))
        return max_area
            
        