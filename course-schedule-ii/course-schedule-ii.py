class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        result = [0] * numCourses	

        indeg = [0] * numCourses
        
        if numCourses == 0:
            return result

        if not prerequisites:
            result = [i for i in range(numCourses)]
            return result


        zero_deg  = deque()

        for pre in prerequisites:
            indeg[pre[0]] += 1

        for i in range(len(indeg)):
            if indeg[i] == 0:
                zero_deg.append(i)
        if not zero_deg:
            return []

        index = 0
        while zero_deg:
            curr = zero_deg.popleft()
            print(index)
            result[index] = curr
            index += 1

            for pre in prerequisites:
                if pre[1] == curr:
                    indeg[pre[0]] -= 1
                    if indeg[pre[0]] == 0:
                        zero_deg.append(pre[0])

        if any(i for i in indeg):
            return []

        return result
