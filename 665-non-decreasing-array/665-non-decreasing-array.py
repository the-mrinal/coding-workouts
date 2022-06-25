class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = False
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                if flag or (i > 1 and i < n-1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                flag = True
        return True

