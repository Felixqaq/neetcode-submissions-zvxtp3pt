class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxN, minN = 1, 1

        for n in nums:
            if n == 0:
                maxN, minN = 1, 1
                continue
            temp = maxN * n
            maxN = max(temp, n*minN, n)
            minN = min(temp, n*minN, n)
            res = max(res, maxN)
        return res