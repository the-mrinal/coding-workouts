class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        
        def checkFeasible(mid,target):
            if arr[mid] >= target:
                return True
            return False
        
        def bSearch(si,ei,target):
            while si < ei:
                mid = si + (ei - si)//2
                
                if checkFeasible(mid,target):
                    ei = mid
                else:
                    si = mid + 1 
            return si
        
        n = len(arr)
        for i in range(n):
            target = arr[i] * 2
            if arr[i] < 0:
                if arr[i]%2 != 0:
                    continue
                target = arr[i]//2

            index = bSearch(i+1,n,target)
            if index < n and arr[index] == target:
                return True
        return False