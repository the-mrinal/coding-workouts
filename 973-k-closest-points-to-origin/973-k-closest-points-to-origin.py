class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a):
            x = a[0]
            y = a[1]
            return math.sqrt(x**2 + y**2)
        maxHeap = []
        
        for index,point in enumerate(points):
            if index >= k and maxHeap:
                if -maxHeap[0][0] > distance(point):
                    heappop(maxHeap)
                    heappush(maxHeap,(-distance(point),point))
            else:
                heappush(maxHeap,(-distance(point),point))
        res = []
        for dist,point in maxHeap:
            res.append(point)
        return res