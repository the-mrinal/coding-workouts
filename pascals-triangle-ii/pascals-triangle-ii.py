class Solution:
    def getRow(self, row: int) -> List[int]:
            if row == 0:
                return [1]
            
            res = self.getRow(row - 1)
            for i in range(len(res)-1 ,0,-1):
                res[i] = res[i] + res[i - 1]
            res.append(1)
            
            return res
        