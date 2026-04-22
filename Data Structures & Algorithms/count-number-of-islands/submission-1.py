class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COLUMN = len(grid[0])
        visited = set()

        def explore(r,c):
            if r>=ROW or c>=COLUMN or min(r,c)<0 or (r,c) in visited or grid[r][c] == '0':
                return 
            grid[r][c]='0'
            visited.add((r,c))
            explore(r+1,c)
            explore(r-1,c)
            explore(r,c+1)
            explore(r,c-1)
        res = 0
        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == '1':
                    explore(i,j)
                    res+=1
        return res
        

        