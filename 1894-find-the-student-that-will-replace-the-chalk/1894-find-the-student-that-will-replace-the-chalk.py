class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        n = len(chalk)
        normalisedK = k % sums
        curr_sum = 0
        for i in range(n):
            curr_sum += chalk[i]
            if curr_sum > normalisedK:
                return i
        return -1