class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            start = i
            target = c - (start * start)
            end = target
            while start < end:
                mid = start + (end - start)//2
                if mid * mid >= target:
                    end = mid
                else:
                    start = mid + 1
            if start*start == target:
                return True
            i += 1
        return False
