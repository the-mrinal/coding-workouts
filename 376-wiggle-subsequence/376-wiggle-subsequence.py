class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0]*len(nums)
        down = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i],up[j] + 1)
        
        return 1 + max(down[len(nums) - 1],up[len(nums) - 1])