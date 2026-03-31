class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        visited = set()
        def backtrack(r,c):
            if r>=row or c>=column or r<0 or c<0 or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))

            perimeter = backtrack(r+1,c) + backtrack(r-1,c)+backtrack(r,c+1)+backtrack(r,c-1)
            return perimeter
        for i in range(row):
            for j in range(column):
                if grid[i][j]==1:
                    return backtrack(i,j)
        return 0
            
        