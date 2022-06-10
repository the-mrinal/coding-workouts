class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        
        while left <= right:
            mid = (left+right)//2
            
            if ord(letters[mid]) <= ord(target):
                left  = mid + 1
            else:
                if mid == left:
                    return letters[left]
                elif ord(letters[mid - 1]) > ord(target):
                    right = mid - 1
                else:
                    return letters[mid]
        
        return letters[0]