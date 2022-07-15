class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dfs(left,right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return dfs(left + 1,right - 1) + 2
            return max(dfs(left+1,right),dfs(left,right - 1))
        
        return dfs(0,n-1)