class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            inserted = float("inf")
            for l, r in intervals:
                if l <= q and r >= q:
                    inserted = min(r - l + 1, inserted)
            res.append(inserted if inserted != float("inf") else -1)
        return res