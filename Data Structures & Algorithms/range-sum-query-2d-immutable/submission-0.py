class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rowSum = [[0]*(len(matrix[0])+1) for _ in range(len(matrix))]
        for i in range(len(self.rowSum)):
            for j in range(1,len(self.rowSum[0])):
                self.rowSum[i][j] = matrix[i][j-1]+self.rowSum[i][j-1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0
        for i in range(row1,row2+1):
            totalSum+=self.rowSum[i][col2+1]-self.rowSum[i][col1]
        return totalSum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)