class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        beinsert = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if beinsert[1] > intervals[i][0]:
                beinsert = [0, min(beinsert[1], intervals[i][1])]
                res += 1
            else:
                beinsert = intervals[i]
        return res