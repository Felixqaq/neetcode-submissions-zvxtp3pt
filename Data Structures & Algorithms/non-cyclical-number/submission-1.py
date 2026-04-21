class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        target = self.deal(n)
        while target != 1:
            if target in visit:
                return False
            visit.add(target)
            target = self.deal(target)
        return True
    
    def deal(self, n):
        res = 0
        while n != 0:
            res += (n%10)**2
            n = n // 10
        print(res)
        return res