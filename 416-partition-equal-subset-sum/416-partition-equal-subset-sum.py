class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s % 2 != 0:
            return False

        s = s//2 
        return self.KnapSack(nums,s)

    def KnapSack(self,nums,C):
        dp = [[False for i in range(C+1)] for i in range(2)]

        for i in range(C+1):
            if i <= nums[0]:
                dp[0][i] = nums[0] == i

        for i in range(1,len(nums)):
            for j in range(1,C+1):
                profitA,profitB = 0,0
                if nums[i] <= j:
                    profitA = dp[(i-1)%2][j - nums[i]]
                profitB = dp[(i-1)%2][j]
                dp[i%2][j] = profitA or profitB

        return dp[(len(nums)-1)%2][C]
