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
    
    def binary_search(self,nums,si,ei,key):
        
        isAsc = nums.get(si) <= nums.get(ei)
        while si <= ei:
            mid = si + (ei - si)//2
            midElem = nums.get(mid)
            if midElem == key:
                return mid		

            if isAsc:
                if midElem < key:
                    si = mid + 1
                else:
                    ei = mid - 1
            else:
                if midElem < key:
                    ei = mid - 1
                else:
                    si = mid + 1
        return float('inf')