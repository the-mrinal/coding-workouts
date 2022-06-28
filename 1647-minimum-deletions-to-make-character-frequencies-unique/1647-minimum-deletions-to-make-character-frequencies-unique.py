class Solution:
    def minDeletions(self, s: str) -> int:
        count,res,used = collections.Counter(s),0,set()
        
        for char,freq in count.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        
        return res