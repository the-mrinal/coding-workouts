class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        startRow = 0
        endRow = row - 1
        startCol = 0
        endCol = col - 1
        ans = []
        j = 0
        while j < row * col:
            # top row
            # print(startCol,endCol,j)
            start = startCol 
            end = endCol
            for i in range(start,end + 1):
                if j < row * col:
                    ans.append(matrix[startRow][i])
                    j += 1

            start = startRow + 1
            end = endRow
            for i in range(start,end ):
                if j < row * col:
                    ans.append(matrix[i][endCol])
                    j += 1

            start = endCol
            end = startCol
            for i in range(start,end,-1):
                if j < row * col:
                    ans.append(matrix[endRow][i])
                    j += 1

            start = endRow
            end = startRow
            for i in range(start,end,-1):
                if j < row * col:
                    ans.append(matrix[i][startRow])
                    j += 1

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1

        return ans