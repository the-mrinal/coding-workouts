class Solution:

        
    
    def countSteps(self,n):
        if n in self.dic:
            return self.dic[n]
        if n % 2:
            self.dic[n] = self.countSteps(3 * n + 1) + 1
        else:
            self.dic[n] = self.countSteps(n // 2) + 1
        return self.dic[n]    

        
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.dic = {1:0}
        for i in range(lo,hi+1):
            self.countSteps(i)
        lst = [(self.dic[i],i) for i in range(lo,hi+1)]
        heapq.heapify(lst)

        for i in range(k):
            ans = heapq.heappop(lst)

        return ans[1]  