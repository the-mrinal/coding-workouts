
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        n = len(weights)
        # maximum capacity(C) where condition(C) is True
        def condition(C):
            totalC,totalD = 0,1
            for i in range(n):
                totalC += weights[i]
                if totalC > C:
                    totalD += 1
                    totalC = weights[i]
                if totalD > days:
                    return False
            return True

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
