class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.large) > len(self.small) + 1:
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * temp)
        
        if len(self.small) > len(self.large) + 1:
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * temp)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -1 * self.small[0]
        return (self.large[0] + -1 * self.small[0]) / 2
        