class Solution:
    def isInterleave(self, m: str, n: str, p: str) -> bool:
        n1 = len(m)
        n2 = len(n)
        n3 = len(p)
        cache = {}
        def dfs(index1,index2,index):
            nonlocal cache
            if index1 == n1 and index2 == n2 and index == n3:
                return True
            if index == n3:
                return False
            key = (index1,index2,index)
            if key not in cache:
                countA,countB  = False,False
                if index1 < n1 and m[index1] == p[index]:
                    countA = dfs(index1+1,index2,index + 1)
                if index2 < n2 and n[index2] == p[index]:
                    countB = dfs(index1,index2 + 1,index + 1)
                cache[key] = countA or countB

            return cache[key]

        return dfs(0,0,0)