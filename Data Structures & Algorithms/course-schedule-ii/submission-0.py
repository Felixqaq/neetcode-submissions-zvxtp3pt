class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            preMap[c1].append(c2)
        
        visit, cycle = set(), set()
        res = []

        def dfs(cls):
            if cls in cycle:
                return False
            
            if cls in visit:
                return True
            
            cycle.add(cls)

            for c in preMap[cls]:
                if not dfs(c):
                    return False
                
            cycle.remove(cls)
            visit.add(cls)
            res.append(cls)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res