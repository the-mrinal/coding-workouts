class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax,maxx = 0,0
        
        for i in range(1,len(prices)):
            print(currMax)
            currMax = max(0,currMax + prices[i] - prices[i - 1])
            maxx = max(currMax,maxx)
            print(currMax,prices[i],prices[i-1])
            
        return maxx