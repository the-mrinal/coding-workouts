'''
#local_max[i] = max(nums[i],nums[i] + local_max[i - 1])

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currMax = 0
        maxSoFar = float('-inf')
        n = len(nums)
        for i in range(n):
            currMax = max(nums[i],nums[i]+currMax)
            maxSoFar = max(currMax,maxSoFar)
        
        return maxSoFar
    '''
    
[-2,1,-3,4,-1,2,1,-5,4]

cM = -2
max = 0

1
1

-2
1

4
4

3
4

5
5

6
6

1
6

5
6


    
    '''