class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def combinations(remaining,comb,nex):
            if remaining == 0:
                ans.append(comb.copy())
            
            else:
                for i in range(nex,n + 1):
                    comb.append(i)
                    combinations(remaining - 1,comb,i+1)
                    comb.pop()
                
        combinations(k,[],1)
        return ans