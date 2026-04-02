class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort()
        i = 0
        res = []
        beinsert = intervals[i]
        for i in range(1, len(intervals)):
            if beinsert[1] < intervals[i][0]:
                res.append(beinsert)
                beinsert = intervals[i]
            else:
                beinsert = [min(beinsert[0], intervals[i][0]), max(beinsert[1], intervals[i][1])]
        res.append(beinsert)
        return res