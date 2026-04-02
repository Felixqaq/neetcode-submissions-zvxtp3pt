class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(s, wordDict):
            if s == "":
                return True
            if s in dp:
                return dp[s]
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    if dfs(s[n:], wordDict):
                        return True
                    else:
                        dp[s[n:]] = False

            return False
        return dfs(s, wordDict)