class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda i:i[0])
        res = {}
        i = 0
        minheap = []
        for q in sorted(queries):
            
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, [r - l + 1, r])
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                res[q] = minheap[0][0]
            else:
                res[q] = -1
        return [res[q] for q in queries]