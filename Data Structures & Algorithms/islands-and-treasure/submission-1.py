class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        row = len(grid)
        column = len(grid[0])
        inf = (2**31)-1
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    q.append((i,j))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if 0<= nr <row and 0 <= nc < column and grid[nr][nc] == inf:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr,nc))

        