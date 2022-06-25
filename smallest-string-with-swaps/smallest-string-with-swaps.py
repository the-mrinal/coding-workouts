class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

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

    def isConnected(self,a,b):
        return self.find(a) == self.find(b)



class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))

        for a,b in pairs:
            uf.union(a,b)

        provinces = defaultdict(list)

        for i in range(len(s)):
            parent = uf.find(i)

            provinces[parent].append([i,s[i]])

        new_str = [0] * len(s)
        for key in provinces:
            values = provinces[key]
            temp = values.copy()
            values.sort(key = lambda x:x[1])

            for i in range(len(values)):
                new_str[temp[i][0]] = values[i][1]

        return ''.join(new_str)
