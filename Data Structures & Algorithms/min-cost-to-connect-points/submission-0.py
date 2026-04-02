class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        N = len(points)
        res = 0
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dis = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])

        minHeap = [[0, 0]]
        visit = set()

        while len(visit) < N:
            dis, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res += dis
            for dis1, j in adj[i]:
                heapq.heappush(minHeap, [dis1, j])
            
        return res