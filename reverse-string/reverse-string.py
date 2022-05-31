class Solution:
    def reverseString(self, s: List[str],index=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def helper(s,e,ls):
            if s >= e:
                return
            
            
            ls[s],ls[e] = ls[e],ls[s]
            
            helper(s+1,e -1,ls)
        
        helper(0,len(s) -1,s)
        