class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = 2 ** 31 - 1
        rev_x = 0
        abs_x = abs(x)
        while abs_x:
            digit = abs_x % 10
            abs_x = abs_x // 10
            if rev_x > LIMIT / 10 or (rev_x == LIMIT/10 and digit > 7) :
                return 0
            curr = (rev_x * 10 + digit)
            rev_x = curr
        return rev_x if x > 0 else -rev_x