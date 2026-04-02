class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                                    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                                                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                                                            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
                                                                    }
        res = []
        part = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(part))
                return
            s_list = mapping[digits[i]]
            for c in s_list:
                part.append(c)
                dfs(i + 1)
                part.pop()
        dfs(0)
        return res