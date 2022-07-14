class Solution:

    def __init__(self, w: List[int]):
        self.totalSum = sum(w)
        self.w = w
        self.n = len(w)
        self.prefix_sum = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sum.append(curr_sum)

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        left = 0
        right = self.n
        while left < right:
            mid = left + (right - left) // 2
            if target <= self.prefix_sum[mid]:
                right = mid
            else:
                left = mid + 1
        return left
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()