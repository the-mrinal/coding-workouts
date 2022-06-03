class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums	
        self.cache = [nums[0]]
        for i in range(1,len(nums)):
            self.cache.append(self.cache[i - 1] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:       
        
        leftVal = 0 if left == 0 else self.cache[left - 1]
        rightVal = self.cache[right]        
        
        return rightVal - leftVal


    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)