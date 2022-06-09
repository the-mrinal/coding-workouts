class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        def isFeasible(mid,curr_target):
            if numbers[mid] >= curr_target:
                return True
            else:
                return False
        
        def bSearch(si,ei,curr_target):
            
            while si < ei:
                mid = si + (ei - si)//2
                if isFeasible(mid,curr_target):
                    ei = mid
                else:
                    si = mid + 1
            return si if numbers[si] == curr_target else None
        
        
        for i in range(n - 1):
            new_target = target - numbers[i]
            new_index = bSearch(i+1,n-1,new_target)
            if new_index:
                return [i+1,new_index+1]
        
        return [None,None]
            
            