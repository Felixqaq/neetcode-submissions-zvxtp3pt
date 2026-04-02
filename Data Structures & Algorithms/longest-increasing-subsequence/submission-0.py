class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sort_nums = []
        
        for n in sorted(nums):
            if len(sort_nums) == 0 or n != sort_nums[-1]:
                sort_nums.append(n)

        numsN = len(nums)
        sortN = len(sort_nums)

        dp = [[0]*(numsN+1) for _ in range(sortN+1)]

        for j in range(1, numsN+1):
            for i in range(1, sortN+1):
                if nums[j-1] == sort_nums[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for d in dp:
            print(d)
        return dp[sortN][numsN]