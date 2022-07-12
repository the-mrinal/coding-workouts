# def mySqrt(x: int) -> int:
#     left, right = 0, x
#     while left < right:
#         mid = left + (right - left) // 2
#         if mid * mid <= x:
#             left = mid + 1
#         else:
#             right = mid
#     return left - 1
class Solution:
    def mySqrt(self, x: int) -> int:

        def condition(mid):
            if mid * mid <= x:
                return False
            return True


        left = 0
        right = x + 1 if x == 1 else x // 2 + 1

        while left < right:
            mid = left + (right - left)//2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left - 1
