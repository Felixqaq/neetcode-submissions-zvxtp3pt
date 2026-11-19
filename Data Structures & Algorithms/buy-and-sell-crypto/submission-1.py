class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < lmin:
                lmin = prices[i]
            res = max(res, prices[i] - lmin)
        return res