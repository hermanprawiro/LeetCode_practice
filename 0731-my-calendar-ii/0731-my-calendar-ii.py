from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.MAX_BOOKING = 2
        self.bookings = SortedDict()
        

    def book(self, start: int, end: int) -> bool:
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1

        count = 0
        for k, v in self.bookings.items():
            count += v
            if count > self.MAX_BOOKING:
                self.bookings[start] -= 1
                self.bookings[end] += 1
                if self.bookings[start] == 0:
                    del self.bookings[start]
                if self.bookings[end] == 0:
                    del self.bookings[end]
                return False
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)