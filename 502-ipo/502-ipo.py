class Solution:
    def __init__(self):
        self.minCapitalHeap = []
        self.maxProfitHeap = []



    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)		
        for i in range(n):
            heappush(self.minCapitalHeap,(capital[i],i))

        availCapital = w	
        for _ in range(k):
            while self.minCapitalHeap and availCapital >= self.minCapitalHeap[0][0]:
                capital,i = heappop(self.minCapitalHeap)
                heappush(self.maxProfitHeap,(-profits[i],i))

            if not self.maxProfitHeap:
                break
            availCapital += -heappop(self.maxProfitHeap)[0]

        return availCapital