class Edge:
    def __init__(self,a,b,cost):
        self.a = a
        self.b = b
        self.cost = cost

    def __lt__(self,other):
        return self.cost < other.cost

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        def costFunction(a,b):
            a_x,a_y = points[a]
            b_x,b_y = points[b]
            return abs(a_x - b_x) + abs(a_y - b_y)


        edgeArr = []
        uf = UnionFind(len(points))

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if i != j:
                    edgeArr.append(Edge(i,j,costFunction(i,j)))
 # Convert pq into a heap.
        heapq.heapify(edgeArr)

        result = 0
        count = len(points) - 1
        while edgeArr and count > 0:
            edge = heapq.heappop(edgeArr)
            if not uf.isConnected(edge.a, edge.b):
                uf.union(edge.a, edge.b)
                result += edge.cost
                count -= 1
        return result