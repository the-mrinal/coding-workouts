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
        indexA = self.orderAgnosticBSearch(mountain_arr,0,index,target)
        indexB = self.orderAgnosticBSearch(mountain_arr,index,n - 1,target)
        
        return min(indexA,indexB) if min(indexA,indexB) < float('inf') else -1 
    
    def findMountain(self,nums):
        # nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]
        
        def checkFeasible(mid):
            midElem = nums.get(mid)
            if  midElem > nums.get(mid - 1): # we have got asc order in our hand.
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
    
    def orderAgnosticBSearch(self,nums,si,ei,target):
        start = nums.get(si)
        end = nums.get(ei)
        def checkFeasible(mid):
            midElem = nums.get(mid)
            if start < midElem or end > midElem: # asc order
                if midElem >= target:
                    return True
                else:
                    return False
            elif start > midElem or end < start: # dsc ordr
                if midElem <= target:
                    return True
                else:
                    return False
            else:
                return True
        
        while si < ei:
            mid = si + (ei - si)//2
            if checkFeasible(mid):
                ei = mid
            else:
                si = mid + 1
        
        return si if nums.get(si) == target else float('inf')