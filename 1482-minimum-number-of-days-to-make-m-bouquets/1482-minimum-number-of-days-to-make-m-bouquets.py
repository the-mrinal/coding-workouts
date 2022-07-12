class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        if  len(bloomDay) < m*k:
            return -1
        def condition(day):
            bouq,flower = 0,0
            for bDay in bloomDay:
                if bDay > day:
                    flower = 0
                else:
                    bouq += (flower + 1) // k
                    flower = (flower + 1) % k
            return bouq >= m
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left