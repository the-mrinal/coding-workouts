class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        count = 0
        intervals.sort()
        for start,end in intervals:
            heappush(minHeap,(start,count,-1))
            heappush(minHeap,(end,count,1)) 
            count += 1
            
        
        roomCount = 0
        maxRoomCount = -1
        while minHeap:
            curr,_,state = heappop(minHeap)
            
            if state == -1:
                roomCount += 1
            else:
                roomCount -= 1
            
            maxRoomCount = max(roomCount,maxRoomCount)
            
        return maxRoomCount
                