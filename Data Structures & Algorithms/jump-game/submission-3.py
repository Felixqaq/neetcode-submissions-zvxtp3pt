class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = nums[0]
        i = 0
        while i <= maxi:
            maxi = max(maxi, i + nums[i])
            i+=1
            if maxi >= len(nums) - 1:
                return True
        return False