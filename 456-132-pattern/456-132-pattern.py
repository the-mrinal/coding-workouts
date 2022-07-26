class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_arr = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            min_arr.append(min(min_arr[i - 1],nums[i]))
        
        for i in range(n - 1,0,-1):
            if nums[i] <= min_arr[i]:
                continue
                
            while stack and stack[-1] <= min_arr[i]:
                stack.pop()
            
            if stack and stack[-1] < nums[i]:
                return True
            
            stack.append(nums[i])
        
        return False