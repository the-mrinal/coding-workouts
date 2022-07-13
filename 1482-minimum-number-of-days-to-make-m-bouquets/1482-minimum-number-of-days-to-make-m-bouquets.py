class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        if  len(bloomDay) < m*k:
            return -1
        def condition(day):
            bouq,flow = 0,0
            for bloom in bloomDay:
                if bloom > day:
                    flow = 0
                else:
                    bouq += (flow + 1)//k
                    flow = (flow + 1) % k
            
            return bouq >= m
        
        while left < right:
            mid = left +(right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
                