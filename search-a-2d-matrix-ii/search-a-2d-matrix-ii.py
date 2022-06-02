class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(si,ei):
            if si[0] > ei[0] or si[0] > len(matrix) - 1 or si[1] > len(matrix[0]) - 1 or si[1] > ei[1]:
                return False

            if si == ei:
                
                return matrix[si[0]][si[1]] == target

            mr = (si[0] + ei[0]) // 2
            mc = (si[1] + ei[1]) // 2

            m = [mr,mc]
            mid = matrix[mr][mc]

            if target < mid:
                # remove last quad
                return helper(si,(mr-1,mc-1)) or helper((si[0],mc),(mr-1,ei[1])) or helper((mr,si[1]), (ei[0],mc - 1))
            elif target > mid:
                return helper((si[0],mc + 1),(mr,ei[1])) or helper((mr+ 1,si[1]), (ei[0],mc)) or helper((mr+1,mc+1),ei)
            
            else:
                return True
            
        return helper((0,0),(len(matrix) -1,len(matrix[0]) -1))
