class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique = set(candyType)
        u = len(unique)
        n = len(candyType) 
        n = n // 2
        if n >= u:
            return u
        else:
            return n 