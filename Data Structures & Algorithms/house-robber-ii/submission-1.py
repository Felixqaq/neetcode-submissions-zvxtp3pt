class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_function(nums[1:]), self.rob_function(nums[:len(nums)-1]))




    def rob_function(self, inum):
        rob1, rob2 = 0, 0
        for n in inum:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
