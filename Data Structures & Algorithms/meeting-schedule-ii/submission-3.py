"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sL, eL = [], []
        for i in intervals:
            sL.append(i.start)
            eL.append(i.end)
        sL.sort()
        eL.sort()

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if sL[s] < eL[e]:
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1
        return res
