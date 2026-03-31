from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr= r+dr
                    nc =c+dc
                    if 0<=nr<row and 0<=nc<column and grid[nr][nc] == 1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            time+=1
        return time if fresh <=0 else -1
        
        