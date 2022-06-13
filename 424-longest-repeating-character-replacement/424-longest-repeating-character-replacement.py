class Solution:
    def characterReplacement(self, str1: str, k: int) -> int:
        window_set ={}
        window_start = 0
        count = 0
        n = len(str1)
        maxReapeating = -1
        max_len = float('-inf')
        for window_end in range(n):
            if str1[window_end] in window_set:
                window_set[str1[window_end]] += 1
            else:
                window_set[str1[window_end]] = 1

            maxReapeating = max(maxReapeating,window_set[str1[window_end]])

            if window_end - window_start + 1 - maxReapeating > k:
                window_set[str1[window_start]] -= 1
                window_start += 1
            max_len = max(max_len,window_end - window_start + 1)

        return max_len