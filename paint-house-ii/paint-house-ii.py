class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        if n == 0: return 0
        # markov chain
        for i in range(1,n):
            min1 = min(costs[i - 1])
            
            index1 = costs[i - 1].index(min1)
            
            min2 = min(costs[i-1][:index1] + costs[i-1][index1 + 1:])
            for j in range(k):
                if j == index1:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        
        return min(costs[n-1])