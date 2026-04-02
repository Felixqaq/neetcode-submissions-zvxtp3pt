class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        def dfs(total, i):
            if total == target:
                if not cur in res:
                    res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])

            dfs(total + candidates[i], i + 1)
            cur.pop()
            dfs(total, i + 1)

        dfs(0, 0)
        return res