class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if preMap[crs] == []:
                return True

            visit.add(crs)

            for c in preMap[crs]:
                if dfs(c) == False:
                    return False

            visit.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True