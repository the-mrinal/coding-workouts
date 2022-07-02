class Solution:

    def partition(self,nums,pivotIndex,low,high):
        pivot = nums[pivotIndex]
        nums[high],nums[pivotIndex] = nums[pivotIndex], nums[high]
        sorted_pivot_index = low	
        for i in range(low,high):
            if nums[i] < pivot:
                nums[i],nums[sorted_pivot_index] = nums[sorted_pivot_index],nums[i]
                sorted_pivot_index += 1
        nums[sorted_pivot_index] ,nums[high] = nums[high],nums[sorted_pivot_index]
        return sorted_pivot_index


    def quickSelect(self,nums,position,low,high):
        if low == high:
            return nums[low]
        pivotIndex = low + (high - low)//2

        pivotSorted = self.partition(nums,pivotIndex,low,high)

        if pivotSorted > position:
            return self.quickSelect(nums,position,low,pivotSorted - 1)
        elif pivotSorted < position:
            return self.quickSelect(nums,position,pivotSorted + 1,high)
        else:
            return nums[pivotSorted] 



    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        kth_smallest = n - k
        return self.quickSelect(nums,kth_smallest,0,n - 1)
