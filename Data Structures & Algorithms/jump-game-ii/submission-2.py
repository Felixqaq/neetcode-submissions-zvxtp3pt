class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 1
        maxs = nums[0]
        curs = nums[0]
        for i in range(len(nums)):
            if i > curs:
                res += 1
                curs = maxs
            maxs = max(maxs, i + nums[i])
        return res