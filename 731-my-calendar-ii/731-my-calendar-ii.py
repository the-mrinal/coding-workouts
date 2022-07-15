class MyCalendarTwo:

    def __init__(self):
        self.calender=[]
        self.overlap = []
        

    def book(self, start: int, end: int) -> bool:
        for a,b in self.overlap:
            if start < b and end > a:
                return False
        for a,b in self.calender:
            if start < b  and end > a:
                self.overlap.append([max(a,start),min(b,end)])
        self.calender.append([start,end])
        return True
                


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)