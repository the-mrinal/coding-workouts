class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def find2Sum(index):
            left = index + 1
            right = n - 1
            
            while left < right:
                if nums[index] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[index] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                find2Sum(i)
        
        return res