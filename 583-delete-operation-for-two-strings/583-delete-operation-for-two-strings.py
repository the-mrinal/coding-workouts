class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        
        dp = {}
        
        def dfs(i,j):
            if i >= m or j >= n:
                return 0    
            key = (i,j)
            if key not in dp:
                dp[key] = 0
                
                if word1[i] == word2[j]:
                    dp[key] = 1 + dfs(i+1,j+1)
                else:
                    dp[key] = max(dfs(i+1,j),dfs(i,j+1))
                
            return dp[key] 

        
        t = dfs(0,0)
        return m + n - 2*t