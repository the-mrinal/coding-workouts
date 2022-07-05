# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         self.caching = {}
#         def dfs(n):
#             if n >= len(nums) - 1:
#                 return True
            
#             if n not in self.caching:
#                 self.caching[n] = False
#                 for i in range(1,nums[n]+1):
#                     self.caching[n] = dfs(n + i)
#                     if self.caching[n]:
#                         return True
#             return self.caching[n]
#         return dfs(0)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if (i + nums[i]) >= lastIndex:
                lastIndex = i
            
        return lastIndex == 0        
