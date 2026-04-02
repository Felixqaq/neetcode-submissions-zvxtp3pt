class Solution:
    def climbStairs(self, n: int) -> int:
        init = [1, 2]
        for i in range(2, n):
            init.append(init[i-1] + init[i-2])
        
        return init[n - 1]
