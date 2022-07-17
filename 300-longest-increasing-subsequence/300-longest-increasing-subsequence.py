'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def dfs(index,prev):
            if index >= n:
                return 0
            key = (index,prev)
            if key not in cache:
                countA,countC = 0,0
                if prev == -1 or nums[prev] < nums[index]:
                    countC = 1 + dfs(index + 1,index)

                countA = dfs(index+1,prev)
                cache[key] = max(countA,countC)
            return cache[key]
        return dfs(0,-1)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],1 + dp[j])
        
        return max(dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        