class Solution:
    def arrangeCoins(self, n: int) -> int:

        sums = 0
        for i in range(n + 1):
            sums += i
            if sums == n:
                return i
            elif sums > n:
                return i - 1