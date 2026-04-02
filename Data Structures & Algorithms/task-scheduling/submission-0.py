class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0 
        q = deque()
        
        while maxheap or q:
            time += 1

            if maxheap:
                task = heapq.heappop(maxheap)
                task += 1
                if task != 0:
                    q.append([task, time+n])

                while q and q[0][1] <= time:
                    temp = q.popleft()
                    heapq.heappush(maxheap, temp[0])

            if q and q[0][1] == time:
                temp = q.popleft()
                heapq.heappush(maxheap, temp[0])
        
        return time