class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        self.rowCaching = []
        for i in range(len(matrix)):
            self.rowCaching.append([])
            sums = 0
            for j in range(len(matrix[i])):
                sums += matrix[i][j]
                self.rowCaching[-1].append(sums)
        print(self.rowCaching)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        localSum = 0
        for i in range(row1,row2 + 1):
            leftVal = col1 - 1 if col1 > 0 else -1
            rightVal = col2
            
            if leftVal == -1:
                localSum += self.rowCaching[i][rightVal] 
            else:
                localSum += (self.rowCaching[i][rightVal] - self.rowCaching[i][leftVal])
        return localSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)