class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for come, to in tickets:
            adj[come].append(to)
        for k in adj:
            adj[k].sort(reverse=True)

        res = []
        def dfs(come):
            while adj[come]:
                to = adj[come].pop()
                dfs(to)
            res.append(come)
        dfs("JFK")
        return res[::-1]