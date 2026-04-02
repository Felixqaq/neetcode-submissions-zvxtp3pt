class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numbers = [0]

        for n in range(1, amount + 1):
            minN = float("inf")
            for coin in coins:
                remain = n - coin 
                if remain >= 0 and numbers[remain] != -1:
                    minN = min(minN, numbers[remain] + 1)
            if minN != float("inf"):
                numbers.append(minN)
            else:
                numbers.append(-1)
        return numbers[amount]