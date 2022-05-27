class Solution:
    # def numSquares(self, n: int) -> int:
#         dp = [0 for _ in range(n + 1)]
#         sum_sq = [i*i for i in range(1,int(math.sqrt(n))+ 1)]
        
#         for i in range(1,n + 1):
#             temp = []
#             for sq in sum_sq:
#                 if sq > i:
#                     break
#                 temp.append(dp[i - sq] + 1)
#             dp[i] = min(temp)
        
#         return dp[n]
#     def numSquares(self, n: int) -> int:
#         sq_nums = set([i*i for i in range(int(n**0.5) + 1)])
        
        
#         def is_divided(n,count):
#             if count == 1:
#                 return n in sq_nums
            
#             for k in sq_nums:
#                 if is_divided(n - k, count - 1):
#                     return True
            
#             return False
        
#         for i in range(1,n+1):
#             if is_divided(n,i):
#                 return i
    def numSquares(self, n: int) -> int:
        sq_nums = [i*i for i in range(1,int(n**0.5) + 1)]
        
        queue = set()
        queue.add(n)
        level = 0
        
        while queue:
            level += 1
            nxt = set()
            for remain in queue:
                for sq in sq_nums:
                    if remain == sq:
                        return level
                    elif remain < sq:
                        break
                    else:
                        nxt.add(remain - sq)
            
            queue = nxt
        
        return level
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                