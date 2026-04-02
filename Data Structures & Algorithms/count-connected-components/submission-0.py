class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e, v in edges:
            adj[e].append(v)
            adj[v].append(e)
        
        visit = set()
        res = 0
        def dfs(i):
            visit.add(i)
            for e in adj[i]:
                if e not in visit:
                    dfs(e)

        for e in range(n):
            if e not in visit:
                dfs(e)
                res += 1

        return res