class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return False
        else:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            
            return True
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Edge:
    def __init__(self,a,b,cost):
        self.p1 = a
        self.p2 = b
        self.cost = cost
    
    def __lt__(self,other):
        return self.cost < other.cost
            
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)
        
        # Convert pq into a heap.
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.connected(edge.p1, edge.p2):
                uf.union(edge.p1, edge.p2)
                result += edge.cost
                count -= 1
        return result
        
        
        
        
        