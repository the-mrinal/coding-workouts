class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        distinctChar = {}
        n = len(s)
        maxLen = 0
        for end in range(n):
            if s[end] in distinctChar:
                prev = start
                start = distinctChar[s[end]] + 1
                while prev < start:
                    del distinctChar[s[prev]]
                    prev += 1
                distinctChar[s[end]] = end
            else:
                distinctChar[s[end]] = end
            
            maxLen = max(maxLen,end - start + 1)
        
        return maxLen