class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countC = {}
        for c in s1:
            countC[c] = 1 + countC.get(c, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            j = len(s1)
            tempC = countC.copy()
            while j != 0:
                j -= 1
                tempC[s2[i + j]] = tempC.get(s2[i + j], 0) - 1
            if not any(tempC.values()):
                return True
        return False