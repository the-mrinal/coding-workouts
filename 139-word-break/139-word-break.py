class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        
        for i in range(n):
            for word in wordDict:
                if ((len(word) - 1 <= i) and (len(word) == i + 1 or dp[i - len(word)])):
                    if s[i - len(word)+1:i+1] == word:
                        dp[i] = True
                        break
        return dp[n - 1]