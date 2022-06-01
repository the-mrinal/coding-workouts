        
#         def helper(t):
#             if t == 1:
#                 return [['0']]
            
#             res = helper(t - 1)
#             curr = []
#             for i in res[-1]:
#                 if i == '0':
#                     curr = curr + ['0','1']
#                 else:
#                     curr = curr + ['1','0']
#             res.append(curr)
#             return res
        
#         res = helper(n)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        mid = (2**(n-1))//2
        
        if k <= mid:
            return self.kthGrammar(n-1,k)
        else:
            return int(not self.kthGrammar(n-1,k-mid))
            
            
            