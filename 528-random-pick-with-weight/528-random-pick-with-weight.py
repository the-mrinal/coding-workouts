class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.w = w
        self.n = len(w)
        currSum = 0
        self.prefix_sum = []
        for i in range(self.n):
            currSum += w[i]
            self.prefix_sum.append(currSum)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        
        left = 0
        right = self.n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.prefix_sum[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
        
        
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()