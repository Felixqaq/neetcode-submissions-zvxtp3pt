class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(i, pre):
            if i in visit:
                return False
            visit.add(i)
            for v in adj[i]:
                if v != pre:
                    if dfs(v, i) == False:
                        return False
            return True

        
        return dfs(0, -1) and len(visit) == n