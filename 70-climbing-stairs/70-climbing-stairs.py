class Solution:
    def climbStairs(self, n: int) -> int:
        
#         def recursion(m):
#             if m == 0:
#                 return 1
#             if m == 1:
#                 return 1
#             if m == 2:
#                 return 2
            
#             return recursion(m-1)+recursion(m-2)
        
        if n <= 1:
            return 1
        if n == 2:
            return 2
        
        count = 0
        curr = 2
        prev = 1
        for i in range(3,n + 1):
            count =(curr + prev)
            prev = curr
            curr = count
        
        return curr
        
        
        # return recursion(n)