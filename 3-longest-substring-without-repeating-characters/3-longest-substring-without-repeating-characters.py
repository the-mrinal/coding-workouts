class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n==1:
            return n
        
        window_start  = window_end = 0
        res = -1
        char = [None] * 256
        while window_end < n:
            index = ord(s[window_end])
            
            if char[index] != None and char[index] >= window_start:
                window_start = char[index] + 1
            
            res = max(res,window_end - window_start + 1)
            
            char[index] = window_end
            window_end += 1
            
        return res