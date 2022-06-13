class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = 0
        window_start = 0
        window_set = {}
        for window_end in range(n):
            if s[window_end] in window_set:
                prev = window_start
                window_start = window_set[s[window_end]] + 1
                while prev < window_start:
                    del window_set[s[prev]]
                    prev += 1
                window_set[s[window_end]] = window_end
            else:
                window_set[s[window_end]] = window_end
            count = max(count,window_end - window_start + 1)
        return count