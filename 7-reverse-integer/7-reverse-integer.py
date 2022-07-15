class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = 2 ** 31 - 1
        rev_x = 0
        abs_x = abs(x)
        while abs_x:
            digit = abs_x % 10
            abs_x = abs_x // 10
            curr = (rev_x * 10 + digit)
            if curr > LIMIT:
                return 0
            else:
                rev_x = curr
        return rev_x if x > 0 else -rev_x