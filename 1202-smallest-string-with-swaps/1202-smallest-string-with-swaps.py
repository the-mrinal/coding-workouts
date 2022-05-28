class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1

            self.count -= 1

            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        uf = UnionFind(len(s))
        
        for a,b in pairs:
            uf.union(a,b)
                
        keyMap = {}
        for i in range(len(uf.root)):
            p_i = uf.find(i)
            
            if p_i not in keyMap:
                keyMap[p_i] = [i]
            else:
                keyMap[p_i].append(i)

                
                
        charArr = [0] * len(s)
        for indices in keyMap.values():
            asciiArr = []
            for index in indices:
                asciiArr.append(ord(s[index]))
            asciiArr.sort()
            i = 0
            for index in indices:
                charArr[index] = chr(asciiArr[i])
                i += 1
        return ''.join(charArr)
