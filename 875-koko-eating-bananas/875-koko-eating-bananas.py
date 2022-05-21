"""
limits: 
left = 1
right = max(piles)

isFeasible(x) # will check if koko will be able to complete all bananas within given hours if he eats x banana / hr

def isFeasible(x):
    return sum(ceil(pile/speed) for pile in piles) <= H



"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFeasible(x):
            return sum(ceil(pile/x) for pile in piles) <= h
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left)//2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left