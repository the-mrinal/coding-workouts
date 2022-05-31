class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        if n in self.cache:
            return self.cache[n]
        
        sums = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        self.cache[n] = sums
        return sums
        