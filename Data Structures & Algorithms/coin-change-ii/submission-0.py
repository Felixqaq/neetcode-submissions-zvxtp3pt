class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0 for _ in range(amount + 1)]
        cur = [1]
        for c in coins[::-1]:
            for i in range(1, amount + 1):
                if i - c >= 0 and i - c < len(cur):
                    cur.append(cur[i-c] + prev[i])
                else:
                    cur.append(prev[i])
            prev = cur
            cur = [1]
        return prev[-1]
