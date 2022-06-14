class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        searcharr = []
        n = len(cardPoints)
        for i in range(k-1,-1,-1):
            searcharr.append(cardPoints[i])
        for j in range(k):
            searcharr.append(cardPoints[n-j-1])
        
        
        window_start = 0
        window_sum = 0
        max_sum = 0
        for window_end in range(len(searcharr)):
            window_sum += searcharr[window_end]
            
            if window_end >= k - 1:
                max_sum = max(window_sum,max_sum)
                window_sum -= searcharr[window_start]
                window_start += 1
        
        return max_sum