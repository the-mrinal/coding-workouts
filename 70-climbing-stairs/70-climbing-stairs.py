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
        
        curr = 1
        prev = 1
        
        for i in range(2,n+1,2):
            temp = curr
            curr = curr + prev
            prev = temp
            if i < n:
                temp = curr
                curr = curr + prev
                prev = temp
        
        return curr