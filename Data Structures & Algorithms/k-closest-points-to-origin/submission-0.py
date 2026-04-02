class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in range(len(points)):
            x = points[i][0] ** 2
            y = points[i][1] ** 2
            dis = x+y
            minheap.append([dis, points[i][0], points[i][1]])
        
        heapq.heapify(minheap)
        res = []
        while k:
            node = heapq.heappop(minheap)

            res.append(node[1:])
            k -= 1

        return res