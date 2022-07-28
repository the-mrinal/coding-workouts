class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        currMax = 0
        maxSoFar = 0
        
        for i in range(1,n):
            currMax = max(0,currMax+prices[i]-prices[i-1])
            maxSoFar = max(currMax,maxSoFar)
        
        return maxSoFar