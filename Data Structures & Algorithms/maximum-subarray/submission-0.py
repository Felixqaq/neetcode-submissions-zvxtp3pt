class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre = 0
        res = nums[0]
        for n in nums:
            res = max(res, pre + n)
            pre = max(0, pre + n)
        return res
