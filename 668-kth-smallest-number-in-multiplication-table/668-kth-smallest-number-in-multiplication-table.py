class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        if k > right:
            return -1

        def condition(num):
            # atleast K val <= target ,min target
            count = 0
            for val in range(1, m + 1):  # count row by row
                add = min(num // val, n)
                if add == 0:  # early exit
                    break
                count += add
            return count >= k   

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
