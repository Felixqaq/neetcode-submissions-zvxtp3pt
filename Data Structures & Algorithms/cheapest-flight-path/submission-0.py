class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for fr, to, dis in flights:
            adj[fr].append([to, dis])
        res = float('inf')
        visit = set()
        def dfs(cur, dis, remain):
            nonlocal res
            if remain == 0 or cur in visit:
                return 
            if cur == dst:
                res = min(res, dis)
                return 
            visit.add(cur)
            for to, inner_dis in adj[cur]:
                dfs(to, dis + inner_dis, remain - 1)
            
            visit.remove(cur)
        
        dfs(src, 0, k + 2)
        return res if res != float('inf') else -1