class MedianFinder:

    def __init__(self):
        self.sortedList = []

    def addNum(self, num: int) -> None:
        self.sortedList.append(num)
        self.sortedList.sort()

    def findMedian(self) -> float:
        mid = len(self.sortedList)/2
        if len(self.sortedList) % 2 != 0:
            return self.sortedList[math.floor(mid)]
        mid = int(mid)
        res = (self.sortedList[mid] + self.sortedList[mid - 1])/2
        return res