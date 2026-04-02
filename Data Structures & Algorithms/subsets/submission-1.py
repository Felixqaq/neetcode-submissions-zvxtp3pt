class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            i+=1
            dfs(i, cur)
            cur.pop()
            dfs(i, cur)
        dfs(0, [])
        return res