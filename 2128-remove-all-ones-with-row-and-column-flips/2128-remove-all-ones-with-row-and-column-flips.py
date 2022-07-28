class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        same,inverted = grid[0],[1-val for val in grid[0]]
        for g in grid:
            if g != same and g != inverted:
                return False
        return True