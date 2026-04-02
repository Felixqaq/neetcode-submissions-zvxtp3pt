class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(nums2):
            if len(nums2) == 1:
                cur.append(nums2[0])
                res.append(cur.copy())
                cur.pop()
                return
                
            for i in range(len(nums2)):
                cur.append(nums2[i])
                print(nums2[:i] + nums2[i+1:])
                dfs(nums2[:i] + nums2[i+1:])
                cur.pop()
            
        dfs(nums)
        return res