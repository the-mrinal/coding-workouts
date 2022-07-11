# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        index = self.findMountain(mountain_arr)
        n = mountain_arr.length()
        indexA = self.binary_search(mountain_arr,0,index,target)
        indexB = self.binary_search(mountain_arr,index,n - 1,target)
        return min(indexA,indexB) if min(indexA,indexB) < float('inf') else -1 
    
    def findMountain(self,nums):
        # nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]
        
        def checkFeasible(mid):
            midElem =  nums.get(mid)
            if midElem > nums.get(mid - 1): # we have got asc order in our hand.
                if midElem < nums.get(mid + 1):
                    return False # left mid + 1
                else:
                    return True #right mid
            else:
                return True # right mid 
        si = 1
        ei = nums.length() - 1
        
        while si < ei:
            mid = si + (ei - si)//2
            
            if checkFeasible(mid):
                ei = mid
            else:
                si = mid + 1
        
        return si
    
    def binary_search(self,arr,start,end, key):
        
        isAscending = arr.get(start) < arr.get(end)
        while start <= end:
            # calculate the middle of the current range
            mid = start + (end - start) // 2
            midElem = arr.get(mid)
            if key == midElem:
                return mid

            if isAscending:  # ascending order
                if key < midElem:
                    end = mid - 1  # the 'key' can be in the first half
                else:  # key > arr[mid]
                    start = mid + 1  # the 'key' can be in the second half
            else:  # descending order
                if key > midElem:
                    end = mid - 1  # the 'key' can be in the first half
                else:  # key < arr[mid]
                    start = mid + 1  # the 'key' can be in the second half

        return float('inf')
    