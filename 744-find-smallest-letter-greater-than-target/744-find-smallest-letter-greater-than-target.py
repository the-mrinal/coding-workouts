class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def isFeasible(mid):
            if letters[mid] > target:
                return True
            return False
        
        left = 0
        right = len(letters) - 1
        
        while left < right:
            mid = left + (right - left)//2
            
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
         
        if left == len(letters) - 1 and letters[left] <= target:
            left = 0
        return letters[left]