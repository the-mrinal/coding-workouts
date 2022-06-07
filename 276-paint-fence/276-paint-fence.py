class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i == 1:
                 return k
            if i == 2:
                 return k * k

            temp =  (k-1) * (dp(i-1) + dp(i-2))
            
            return temp
	
        return dp(n)