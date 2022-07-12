class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def condition(speed):
            return sum([math.ceil(pile/speed) for pile in piles]) <= h

        while left < right:
            mid = left + (right - left)// 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left

