class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        
        while i < len(first) and j < len(second):
            
            lo = max(first[i][0],second[j][0])
            hi = min(first[i][1],second[j][1])
            
            if lo <= hi:
                ans.append((lo,hi))
                
            if first[i][1] < second[j][1]:
                i += 1
            else:
                j += 1
                
        
        return ans