class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 2 4 1 2 5
        # 0 2 3
        weak = []
        for i in range(len(mat)):
            score = sum(mat[i])
            weak.append([score,i])
        weak.sort()
        indexes = []
        for i in range(k):
            indexes.append(weak[i][1])
        
        return indexes