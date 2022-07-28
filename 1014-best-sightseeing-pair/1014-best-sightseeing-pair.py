'''
8 1 5 2 6

a[i] + a[j] - (j - i)

prev = a[0] - 1
1 to n
    curr = max(curr+prev,)




'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        maxSoFar = 0
        curr = 0
        
        for i in range(n):
            maxSoFar = max(maxSoFar,curr+values[i])
            
            curr = max(curr,values[i]) - 1
            
        return maxSoFar