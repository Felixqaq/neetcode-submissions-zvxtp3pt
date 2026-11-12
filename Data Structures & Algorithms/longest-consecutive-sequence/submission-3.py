class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        
        print(nums)
        res = 0
        temp = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i + 1]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
        
        return max(res, temp)
                