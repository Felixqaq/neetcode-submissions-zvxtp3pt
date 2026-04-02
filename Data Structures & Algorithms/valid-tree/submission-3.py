class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges.sort()
        if edges == []:
            return True
        graph = set()
        haveRoot = False
        for e1, e2 in edges:
            if e1 == e2:
                return False
            if e1 in graph and e2 in graph:
                return False
            if e1 not in graph and e2 not in graph:
                if haveRoot:
                    return False
                haveRoot = True
            graph.add(e1)
            graph.add(e2)

        if len(graph) != n:
            return False
        return True