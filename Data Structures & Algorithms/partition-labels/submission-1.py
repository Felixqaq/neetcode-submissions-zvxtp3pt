class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dp = {}
        for i, c in enumerate(s):
            if i >= dp.get(c, 0):
                dp[c] = i
        l, r = 0, dp[s[0]]
        res = []
        for i, c in enumerate(s):
            r = max(dp[c], r)
            if i == r:
                res.append(r - l + 1)
                l = i + 1
            
        return res