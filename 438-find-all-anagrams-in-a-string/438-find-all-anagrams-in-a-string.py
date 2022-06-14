class Solution:
    def findAnagrams(self, str1: str, pattern: str) -> List[int]:
        res = []
        window_start = 0
        k = len(pattern)
        freq = {}
        for i in range(k):
            if pattern[i] in freq:
                freq[pattern[i]] += 1
            else:
                freq[pattern[i]] = 1

        n = len(str1)
        for window_end in range(n):
            if str1[window_end] in freq:
                freq[str1[window_end]] -= 1

            if window_end > k - 1:
                if str1[window_start] in freq:
                    freq[str1[window_start]] += 1
                window_start += 1

            if len(set(freq.values())) == 1 and sum(freq.values()) == 0:
                res.append(window_start)
        return res