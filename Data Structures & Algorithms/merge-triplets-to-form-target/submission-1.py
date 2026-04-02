class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mx, my, mz = 0, 0, 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                mx = max(x, mx)
                my = max(y, my)
                mz = max(z, mz)
        
        return [mx, my, mz] == target