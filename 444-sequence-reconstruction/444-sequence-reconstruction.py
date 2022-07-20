class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        '''
        
        Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
        Output: false
        
        indeg = 1:0 |2:1 | 3:1
        adjMap = 1:[2,3],2:[],3:[]
        
        que = deque()
        
        for key,val in indeg.items():
            if val == 0:
                que.append(key)
        
        if at any point there are more than one src then its false.
        
        [4,1,5,2,6,3]
        [[5,2,6,3],[4,1,5,2]]
        '''
        n = len(nums)
        indeg = {i:0 for i in range(1,n + 1)}
        adjMap = {i:[] for i in range(1,n + 1)}
        
        
        # for pre,main in sequences:
        #     adjMap[pre].append(main)
        #     indeg[main] += 1
        
        for seq in sequences:
            for pre in range(len(seq) - 1):
                adjMap[seq[pre]].append(seq[pre + 1])
                indeg[seq[pre + 1]] += 1
                
        
        
        que = deque()
        
        for key,val in indeg.items():
            if val == 0:
                que.append(key)

        res = []
        while que:
            if len(que) > 1:
                return False
            if nums[len(res)] != que[0]:
                return False
            curr = que.popleft()
            res.append(curr)
            
            for child in adjMap[curr]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    que.append(child)

        
        return len(res) == len(nums)
            
            
            
            
        
        
        
        
        
        