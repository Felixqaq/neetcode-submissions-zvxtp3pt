class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = -1 * heapq.heappop(stones)
            max2 = -1 * heapq.heappop(stones)
            res = (max1-max2) * -1
            heapq.heappush(stones, res)
        return stones[0] * -1