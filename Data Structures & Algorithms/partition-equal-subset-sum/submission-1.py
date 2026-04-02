class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        if sum(nums) % 2 != 0:
            return False
        if half in nums: return True

        def dfs(innums, target):
            if innums == []:
                return False
            if target - innums[0] in innums[1:]:
                return True
            return dfs(innums[1:], target - innums[0]) or dfs(innums[1:], target)
        return dfs(nums, half)

