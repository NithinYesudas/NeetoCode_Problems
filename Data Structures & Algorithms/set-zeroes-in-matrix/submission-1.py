class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        res = [r.copy() for r in matrix]
        def helper(i,j):
            for r in range(row):
                res[r][j] = 0
            for c in range(column):
                res[i][c] = 0
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    helper(i,j)
        matrix.clear()
        matrix.extend(res)

        
        
        