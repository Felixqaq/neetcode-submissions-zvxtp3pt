class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        count = set()
        while r < len(s):
            if s[r] in count:
                res = max(res, r-l)
                while s[l] != s[r]:
                    count.remove(s[l])
                    l += 1
                l += 1
            count.add(s[r])
            r += 1

        return max(res, r-l)