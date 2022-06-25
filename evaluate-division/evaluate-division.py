class CustomUnionFind:
    def __init__(self):
        self.root_weights = {}

    def find(self,x):
        if x not in self.root_weights:
            self.root_weights[x] = (x,1)
        ids,w = self.root_weights[x]
        if ids != x:
            parent_id,parent_w = self.find(ids)
            self.root_weights[x] = (parent_id,w * parent_w)
        return self.root_weights[x]

    def union(self,a,b,val):
        rootA,wA = self.find(a)
        rootB,wB = self.find(b)

        if rootA != rootB:
            self.root_weights[rootA] = (rootB, wB* val / wA)


# evaluate division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):

        uf = CustomUnionFind()

        for (x,y),val in zip(equations,values):
            uf.union(x,y,val)


        res = []
        for x,y in queries:
            if x not in uf.root_weights or y not in uf.root_weights:
                res.append(-1)
            else:
                rootX,wX = uf.find(x)
                rootY,wY = uf.find(y)

                if rootX != rootY:
                    res.append(-1)
                else:
                    res.append(wX/wY)

        return res
