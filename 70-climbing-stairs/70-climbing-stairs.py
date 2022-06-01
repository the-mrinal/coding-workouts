class Solution:
    
    def __init__(self):
        self.cache = {}
    
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 2:
#             return n
        
#         if n in self.cache:
#             return self.cache[n]
        
#         sums = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
#         self.cache[n] = sums
#         return sums
        
    def climbStairs(self,n:int) -> int:
        if n <= 2:
            return n
        res = [0 for _ in range(n + 1)]
        
        res[0] = 1
        res[1] = 1
        res[2] = 2
        
        for i in range(2,n+1,2):
            res[i] = res[i - 1] + res[i - 2]
            if i < n:
                res[i + 1] = res[i] + res[i - 1]
        
        return res[n]