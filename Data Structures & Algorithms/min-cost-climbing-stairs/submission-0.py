class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pay = [0, 0]
        for i in range(2, len(cost)+1):
            pay.append(min(pay[i - 1] + cost[i - 1], pay[i - 2] + cost[i - 2]))
        return pay[-1]